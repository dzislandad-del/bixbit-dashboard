"""seo_common.py — общий код для скриптов в scripts/.

- load_env: читает .env (секреты не печатаются);
- CTX: TLS-контекст с CA (python.org-сборки на macOS не видят системные CA);
- google_token: access token service account (JWT подписывается openssl,
  приватный ключ живёт только во временной папке 0700).
"""
import base64, json, os, shutil, ssl, subprocess, tempfile, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(ROOT, ".env")


def ssl_context():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        pass
    if os.path.exists("/etc/ssl/cert.pem"):
        return ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    return ssl.create_default_context()


CTX = ssl_context()

# Ожидаемые проблемы Яндекс.Вебмастера по хосту — не алертить.
# bixbit.io заблокирован в РФ решением суда (РКН); российская аудитория ходит на bixbit.tech.
YANDEX_EXPECTED = {"bixbit.io": {"CONNECT_FAILED", "NO_ROBOTS_TXT"}}


def yandex_expected(diag):
    """Набор ожидаемых проблем для хоста из JSON диагностики yandex-query.py."""
    url = (diag.get("host") or {}).get("ascii_host_url") or ""
    host = url.split("://")[-1].strip("/").split(":")[0]
    return YANDEX_EXPECTED.get(host, set())


def load_env(path=ENV_PATH):
    env = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    # переменные окружения (напр. в CI) имеют приоритет над .env
    env.update({k: v for k, v in os.environ.items() if k in env or k.startswith(("GSC_", "GA4_", "DATAFORSEO_", "BING_", "GOOGLE_"))})
    return env


def _b64url(b):
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def google_token(sa_path, scopes):
    sa = json.load(open(os.path.expanduser(sa_path)))
    token_uri = sa.get("token_uri", "https://oauth2.googleapis.com/token")
    now = int(time.time())
    header = _b64url(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    claims = _b64url(json.dumps({"iss": sa["client_email"], "scope": " ".join(scopes),
                                 "aud": token_uri, "iat": now, "exp": now + 600}).encode())
    unsigned = f"{header}.{claims}".encode()
    tmp = tempfile.mkdtemp()
    os.chmod(tmp, 0o700)
    try:
        key = os.path.join(tmp, "sa.key")
        fd = os.open(key, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        os.write(fd, sa["private_key"].encode())
        os.close(fd)
        sig = subprocess.run(["openssl", "dgst", "-sha256", "-sign", key],
                             input=unsigned, capture_output=True, check=True).stdout
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    body = urllib.parse.urlencode({"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                                   "assertion": f"{unsigned.decode()}.{_b64url(sig)}"}).encode()
    with urllib.request.urlopen(urllib.request.Request(token_uri, data=body), timeout=30, context=CTX) as r:
        return json.load(r)["access_token"]
