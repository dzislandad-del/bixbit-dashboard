#!/usr/bin/env bash
# check-connectors.sh — проверка источников данных SEO (RUNBOOK.md §2).
#
# Делает по одному лёгкому тестовому запросу к GSC, GA4, PageSpeed, CrUX,
# Moz и Bing Webmaster и печатает только статусы.
# Ключи, токены и приватные ключи не выводятся и не попадают в аргументы
# процессов: curl получает их через конфиг-файл во временной папке (chmod 700),
# которая удаляется при выходе. Любой секрет в тексте ошибок API заменяется на ***.
#
# Использование:  ./scripts/check-connectors.sh [путь/к/.env]
# Зависимости:    bash 3.2+, curl, openssl, python3 (всё есть в macOS).
# Код выхода:     0 — ошибок нет, 1 — есть FAIL, 2 — не найден .env.

set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="${1:-$ROOT/.env}"
TEST_URL="https://bixbit.io/en"
TEST_ORIGIN="https://bixbit.io"

TMP="$(mktemp -d)"
chmod 700 "$TMP"
trap 'rm -rf "$TMP"' EXIT

if [[ ! -f "$ENV_FILE" ]]; then
  echo "ERROR: $ENV_FILE не найден" >&2
  exit 2
fi
set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

ACCESS_TOKEN=""
export ACCESS_TOKEN
N_OK=0; N_WARN=0; N_FAIL=0; N_SKIP=0

# --- helpers -----------------------------------------------------------------

# Переменная задана и не является заглушкой из .env.example?
is_set() {
  local v="${!1:-}"
  [[ -n "$v" && "$v" != your_* && "$v" != "000000000" && "$v" != */Users/you/* ]]
}

# report STATUS NAME HTTP_CODE MESSAGE
report() {
  case "$1" in
    OK)   N_OK=$((N_OK + 1)) ;;
    WARN) N_WARN=$((N_WARN + 1)) ;;
    FAIL) N_FAIL=$((N_FAIL + 1)) ;;
    SKIP) N_SKIP=$((N_SKIP + 1)) ;;
  esac
  printf '%-7s %-10s %-4s %s\n' "[$1]" "$2" "$3" "${4:-}"
}

b64url() { openssl base64 -A | tr '+/' '-_' | tr -d '='; }

# request METHOD URL [BODY_FILE] [CONTENT_TYPE]
# Заголовки берутся из массива HDRS. Тело ответа -> $TMP/body, stdout -> HTTP-код.
request() {
  local method="$1" url="$2" body="${3:-}" ctype="${4:-application/json}"
  local cfg="$TMP/curl.cfg" h code
  rm -f "$TMP/body"
  {
    printf 'url = "%s"\n' "$url"
    for h in ${HDRS[@]+"${HDRS[@]}"}; do printf 'header = "%s"\n' "$h"; done
    if [[ -n "$body" ]]; then
      printf 'header = "Content-Type: %s"\n' "$ctype"
      printf 'data-binary = "@%s"\n' "$body"
    fi
  } > "$cfg"
  code=$(curl -sS -m "${TIMEOUT:-30}" -X "$method" --config "$cfg" \
    -o "$TMP/body" -w '%{http_code}' 2>/dev/null) || true
  rm -f "$cfg"
  echo "${code:-000}"
}

# py 'выражение' — вычисляет выражение над d (JSON-тело последнего ответа),
# вычищает секреты и обрезает до 160 символов.
py() {
  python3 - "$TMP/body" "$1" <<'EOF'
import json, os, sys
raw = open(sys.argv[1], errors="replace").read() if os.path.exists(sys.argv[1]) else ""
try:
    d = json.loads(raw)
except Exception:
    d = {"_raw": " ".join(raw.split())}
try:
    out = eval(sys.argv[2], {"d": d})
except Exception:
    out = ""
s = "" if out is None else str(out)
for k in ("PAGESPEED_API_KEY", "YANDEX_WEBMASTER_TOKEN", "MOZ_API_TOKEN", "MOZ_ACCESS_ID", "MOZ_SECRET_KEY",
          "BING_WEBMASTER_API_KEY", "ACCESS_TOKEN"):
    v = os.environ.get(k)
    if v and len(v) > 3:
        s = s.replace(v, "***")
print(s.replace("\n", " ")[:160])
EOF
}

# Текст ошибки из ответа любого из API.
err() {
  local m
  if [[ ! -s "$TMP/body" ]]; then echo "нет ответа (сеть/таймаут/DNS)"; return; fi
  m=$(py "((d.get('error', {}).get('message') if isinstance(d.get('error'), dict) else d.get('error')) or d.get('error_description') or d.get('message') or d.get('Message') or '')")
  [[ -z "$m" ]] && m=$(py "('не JSON: ' + d['_raw'][:120]) if d.get('_raw') else ''")
  echo "${m:-нет JSON-описания ошибки}"
}

body_json() { printf '%s' "$1" > "$TMP/req.json"; echo "$TMP/req.json"; }

# --- Google OAuth (service account -> access token, один на GSC + GA4) --------

GOOGLE_OK=0; GT_CODE="-"; GT_ERR=""; SA_EMAIL=""

google_token() {
  local sa="${GOOGLE_APPLICATION_CREDENTIALS/#\~/$HOME}"
  if [[ ! -f "$sa" ]]; then GT_ERR="файл service account не найден по пути из .env"; return 1; fi

  if ! python3 - "$sa" "$TMP" <<'EOF'
import json, os, sys
d = json.load(open(sys.argv[1]))
fd = os.open(os.path.join(sys.argv[2], "sa.key"), os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
os.write(fd, d["private_key"].encode())
os.close(fd)
with open(os.path.join(sys.argv[2], "sa.meta"), "w") as f:
    f.write(d["client_email"] + "\n" + d.get("token_uri", "https://oauth2.googleapis.com/token") + "\n")
EOF
  then GT_ERR="не удалось разобрать JSON service account"; return 1; fi

  local token_uri now scope hdr claims unsigned sig
  { read -r SA_EMAIL; read -r token_uri; } < "$TMP/sa.meta"
  now=$(date +%s)
  scope="https://www.googleapis.com/auth/webmasters.readonly https://www.googleapis.com/auth/analytics.readonly"
  hdr=$(printf '%s' '{"alg":"RS256","typ":"JWT"}' | b64url)
  claims=$(printf '{"iss":"%s","scope":"%s","aud":"%s","iat":%d,"exp":%d}' \
    "$SA_EMAIL" "$scope" "$token_uri" "$now" $((now + 600)) | b64url)
  unsigned="$hdr.$claims"
  if ! sig=$(printf '%s' "$unsigned" | openssl dgst -sha256 -sign "$TMP/sa.key" 2>/dev/null | b64url) || [[ -z "$sig" ]]; then
    rm -f "$TMP/sa.key"; GT_ERR="openssl не смог подписать JWT"; return 1
  fi
  rm -f "$TMP/sa.key"
  printf 'grant_type=urn%%3Aietf%%3Aparams%%3Aoauth%%3Agrant-type%%3Ajwt-bearer&assertion=%s' \
    "$unsigned.$sig" > "$TMP/req.form"

  HDRS=()
  GT_CODE=$(request POST "$token_uri" "$TMP/req.form" application/x-www-form-urlencoded)
  rm -f "$TMP/req.form"
  ACCESS_TOKEN=$(python3 -c 'import json,sys
try: print(json.load(open(sys.argv[1])).get("access_token", ""))
except Exception: print("")' "$TMP/body")
  export ACCESS_TOKEN
  if [[ "$GT_CODE" != 200 || -z "$ACCESS_TOKEN" ]]; then GT_ERR="$(err)"; return 1; fi
}

google_guard() { # google_guard NAME VAR -> 0 если можно проверять
  if ! is_set "$2"; then report SKIP "$1" - "$2 не задан в .env"; return 1; fi
  if ! is_set GOOGLE_APPLICATION_CREDENTIALS; then report SKIP "$1" - "GOOGLE_APPLICATION_CREDENTIALS не задан в .env"; return 1; fi
  if [[ $GOOGLE_OK != 1 ]]; then report FAIL "$1" "$GT_CODE" "OAuth: $GT_ERR"; return 1; fi
}

# --- checks ------------------------------------------------------------------

check_gsc() {
  google_guard GSC GSC_SITE_URL || return
  local site code perm
  site=$(python3 -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1], safe=""))' "$GSC_SITE_URL")
  HDRS=("Authorization: Bearer $ACCESS_TOKEN")
  code=$(request GET "https://www.googleapis.com/webmasters/v3/sites/$site")
  if [[ "$code" == 200 ]]; then
    perm=$(py "d.get('permissionLevel', '?')")
    if [[ "$perm" == siteUnverifiedUser ]]; then
      report WARN GSC "$code" "$GSC_SITE_URL: права siteUnverifiedUser — данных не будет"
    else
      report OK GSC "$code" "$GSC_SITE_URL, права: $perm"
    fi
  elif [[ "$code" == 403 || "$code" == 404 ]]; then
    report FAIL GSC "$code" "$(err) → добавь service account в GSC: Settings → Users and permissions"
  else
    report FAIL GSC "$code" "$(err)"
  fi
}

check_ga4() {
  google_guard GA4 GA4_PROPERTY_ID || return
  local code
  HDRS=("Authorization: Bearer $ACCESS_TOKEN")
  code=$(request POST "https://analyticsdata.googleapis.com/v1beta/properties/$GA4_PROPERTY_ID:runReport" \
    "$(body_json '{"dateRanges":[{"startDate":"7daysAgo","endDate":"yesterday"}],"metrics":[{"name":"sessions"}]}')")
  if [[ "$code" == 200 ]]; then
    report OK GA4 "$code" "property $GA4_PROPERTY_ID, sessions за 7 дней: $(py "d['rows'][0]['metricValues'][0]['value'] if d.get('rows') else 0")"
  elif [[ "$code" == 403 ]]; then
    report FAIL GA4 "$code" "$(err) → дай service account роль Viewer в GA4: Admin → Property access"
  else
    report FAIL GA4 "$code" "$(err)"
  fi
}

check_pagespeed() {
  if ! is_set PAGESPEED_API_KEY; then report SKIP PageSpeed - "PAGESPEED_API_KEY не задан в .env"; return; fi
  local code
  HDRS=("X-Goog-Api-Key: $PAGESPEED_API_KEY")
  code=$(TIMEOUT=120 request GET \
    "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=$TEST_URL&strategy=mobile&category=performance")
  if [[ "$code" == 200 ]]; then
    report OK PageSpeed "$code" "$TEST_URL mobile perf=$(py "round(d['lighthouseResult']['categories']['performance']['score'] * 100)"), поле CrUX: $(py "d.get('loadingExperience', {}).get('overall_category', 'нет данных')")"
  else
    report FAIL PageSpeed "$code" "$(err)"
  fi
}

check_crux() {
  if ! is_set PAGESPEED_API_KEY; then report SKIP CrUX - "PAGESPEED_API_KEY не задан в .env"; return; fi
  local code
  HDRS=("X-Goog-Api-Key: $PAGESPEED_API_KEY")
  # JSON собираем через printf: в bash 3.2 "{a,b}" внутри вложенной $(...) раскрывается как brace expansion.
  local crux_body
  crux_body=$(printf '{"origin":"%s","formFactor":"PHONE"}' "$TEST_ORIGIN")
  code=$(request POST "https://chromeuxreport.googleapis.com/v1/records:queryRecord" "$(body_json "$crux_body")")
  case "$code" in
    200) report OK CrUX "$code" "$TEST_ORIGIN PHONE LCP p75=$(py "d['record']['metrics']['largest_contentful_paint']['percentiles']['p75']")ms" ;;
    404) report WARN CrUX "$code" "ключ рабочий, но у $TEST_ORIGIN нет полевых данных CrUX" ;;
    403) report FAIL CrUX "$code" "$(err) → включи Chrome UX Report API в Google Cloud для этого ключа" ;;
    *)   report FAIL CrUX "$code" "$(err)" ;;
  esac
}

check_moz() {
  local code
  # Новый Moz API (api.moz.com, JSON-RPC, токен в x-moz-token) — для аккаунтов с 2024+.
  if is_set MOZ_API_TOKEN; then
    HDRS=("x-moz-token: $MOZ_API_TOKEN")
    code=$(request POST "https://api.moz.com/jsonrpc" "$(body_json \
      '{"jsonrpc":"2.0","id":"check-connectors","method":"data.site.metrics.fetch","params":{"data":{"site_query":{"query":"bixbit.io","scope":"domain"}}}}')")
    if [[ "$code" == 200 && -z "$(py "d.get('error') or ''")" ]]; then
      report OK Moz "$code" "Moz API (token): bixbit.io DA=$(py "(d.get('result', {}).get('site_metrics') or {}).get('domain_authority', '?')")"
    elif [[ "$code" == 200 ]]; then
      report FAIL Moz "$code" "JSON-RPC: $(py "(d.get('error') or {}).get('message', d.get('error'))")"
    elif [[ "$code" == 401 || "$code" == 403 ]]; then
      report FAIL Moz "$code" "$(err) → проверь MOZ_API_TOKEN в дашборде Moz API"
    else
      report FAIL Moz "$code" "$(err)"
    fi
    return
  fi
  # Legacy Links API v2 (Access ID + Secret Key, Basic Auth).
  if ! is_set MOZ_ACCESS_ID || ! is_set MOZ_SECRET_KEY; then
    report SKIP Moz - "MOZ_API_TOKEN (или legacy MOZ_ACCESS_ID / MOZ_SECRET_KEY) не задан в .env"; return
  fi
  HDRS=("Authorization: Basic $(printf '%s:%s' "$MOZ_ACCESS_ID" "$MOZ_SECRET_KEY" | openssl base64 -A)")
  code=$(request POST "https://lsapi.seomoz.com/v2/url_metrics" "$(body_json '{"targets":["bixbit.io/"]}')")
  case "$code" in
    200)     report OK Moz "$code" "legacy v2: bixbit.io DA=$(py "d['results'][0].get('domain_authority', '?')")" ;;
    401|403) report FAIL Moz "$code" "$(err) → legacy-ключи не подошли; для нового аккаунта задай MOZ_API_TOKEN" ;;
    *)       report FAIL Moz "$code" "$(err)" ;;
  esac
}

check_bing() {
  if ! is_set BING_WEBMASTER_API_KEY; then report SKIP Bing - "BING_WEBMASTER_API_KEY не задан в .env"; return; fi
  local code
  HDRS=()
  code=$(request GET "https://ssl.bing.com/webmaster/api.svc/json/GetUserSites?apikey=$BING_WEBMASTER_API_KEY")
  if [[ "$code" == 200 ]]; then
    report OK Bing "$code" "$(py "'сайтов: %d, bixbit.io: %s' % (len(d.get('d') or []), next(('verified' if s.get('IsVerified') else 'не верифицирован') for s in (d.get('d') or []) if 'bixbit.io' in s.get('Url', '')) if any('bixbit.io' in s.get('Url', '') for s in (d.get('d') or [])) else 'не найден')")"
  else
    report FAIL Bing "$code" "$(err)"
  fi
}

check_yandex() {
  if ! is_set YANDEX_WEBMASTER_TOKEN; then report SKIP Yandex - "YANDEX_WEBMASTER_TOKEN не задан в .env"; return; fi
  local code uid
  HDRS=("Authorization: OAuth $YANDEX_WEBMASTER_TOKEN")
  code=$(request GET "https://api.webmaster.yandex.net/v4/user")
  if [[ "$code" != 200 ]]; then
    report FAIL Yandex "$code" "$(err) → проверь токен (права webmaster:hostinfo)"; return
  fi
  uid=$(py "d.get('user_id', '')")
  code=$(request GET "https://api.webmaster.yandex.net/v4/user/$uid/hosts")
  if [[ "$code" == 200 ]]; then
    report OK Yandex "$code" "$(py "'сайтов: %d, bixbit.io: %s' % (len(d.get('hosts') or []), next(('verified' if h.get('verified') else 'НЕ подтверждён') for h in (d.get('hosts') or []) if 'bixbit.io' in h.get('ascii_host_url','') and 'bixbitusa' not in h.get('ascii_host_url','')) if any('bixbit.io' in h.get('ascii_host_url','') and 'bixbitusa' not in h.get('ascii_host_url','') for h in (d.get('hosts') or [])) else 'не добавлен')")"
  else
    report FAIL Yandex "$code" "$(err)"
  fi
}

# --- main --------------------------------------------------------------------

echo "Проверка коннекторов — $(date '+%Y-%m-%d %H:%M')"
if is_set GOOGLE_APPLICATION_CREDENTIALS && { is_set GSC_SITE_URL || is_set GA4_PROPERTY_ID; }; then
  if google_token; then GOOGLE_OK=1; fi
  [[ -n "$SA_EMAIL" ]] && echo "Service account: $SA_EMAIL"
fi
echo

check_gsc
check_ga4
check_pagespeed
check_crux
check_moz
check_bing
check_yandex

echo
echo "Итого: OK=$N_OK WARN=$N_WARN FAIL=$N_FAIL SKIP=$N_SKIP"
[[ $N_FAIL -eq 0 ]]
