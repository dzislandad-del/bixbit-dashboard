#!/usr/bin/env python3
"""google_ads_refresh_token.py — выпустить новый refresh token для Google Ads API
и сразу записать его в секреты GitHub (значения на экран не выводятся).

Запуск на своём компьютере (нужны python3 и gh, вход в gh выполнен):
  python3 scripts/google_ads_refresh_token.py

Скрипт спросит Client ID и Client Secret OAuth-клиента (Google Cloud Console →
APIs & Services → Credentials), откроет браузер для входа в Google-аккаунт,
у которого есть доступ к рекламному аккаунту, и сохранит в репозиторий
dzislandad-del/bixbit-dashboard секреты:
  GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET, GOOGLE_ADS_REFRESH_TOKEN

Если браузер покажет redirect_uri_mismatch — добавьте в OAuth-клиент
Authorized redirect URI:  http://127.0.0.1:8765/
(или создайте клиент типа «Desktop app» — ему URI добавлять не нужно).
"""
import getpass, http.server, json, secrets, subprocess, sys, threading, urllib.error, urllib.parse, urllib.request, webbrowser

REPO = "dzislandad-del/bixbit-dashboard"
PORT = 8765
REDIRECT = f"http://127.0.0.1:{PORT}/"
SCOPE = "https://www.googleapis.com/auth/adwords"


def main():
    cid = input("Client ID: ").strip()
    csec = getpass.getpass("Client Secret (ввод скрыт): ").strip()
    if not cid or not csec:
        sys.exit("Client ID и Client Secret обязательны")

    state = secrets.token_urlsafe(16)
    got = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if q.get("state", [""])[0] != state:
                self.send_response(400); self.end_headers(); return
            got.update({k: v[0] for k, v in q.items()})
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers()
            self.wfile.write("<h3>Готово — вернитесь в терминал.</h3>".encode())

        def log_message(self, *a):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", PORT), H)
    t = threading.Thread(target=srv.handle_request, daemon=True); t.start()

    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": REDIRECT, "response_type": "code", "scope": SCOPE,
        "access_type": "offline", "prompt": "consent", "state": state})
    print("\nОткрываю браузер. Войдите в Google-аккаунт с доступом к Google Ads и разрешите доступ.")
    print("Если браузер не открылся, откройте ссылку вручную:\n" + url + "\n")
    webbrowser.open(url)
    t.join(timeout=300)
    srv.server_close()
    if "code" not in got:
        sys.exit("Код авторизации не получен: " + got.get("error", "таймаут 5 минут"))

    body = urllib.parse.urlencode({"code": got["code"], "client_id": cid, "client_secret": csec,
                                   "redirect_uri": REDIRECT, "grant_type": "authorization_code"}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=body), timeout=30) as r:
            tok = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit("Ошибка обмена кода: " + e.read().decode(errors="replace")[:300])
    rt = tok.get("refresh_token")
    if not rt:
        sys.exit("Google не вернул refresh_token — отзовите доступ приложения на myaccount.google.com/permissions и повторите")

    for name, val in (("GOOGLE_ADS_CLIENT_ID", cid), ("GOOGLE_ADS_CLIENT_SECRET", csec), ("GOOGLE_ADS_REFRESH_TOKEN", rt)):
        subprocess.run(["gh", "secret", "set", name, "-R", REPO], input=val.encode(), check=True,
                       stdout=subprocess.DEVNULL)
        print(f"✓ {name} обновлён в {REPO}")
    print("\nГотово. Чтобы токен не истекал каждые 7 дней, переведите OAuth consent screen "
          "в Google Cloud в статус «In production».")


if __name__ == "__main__":
    main()
