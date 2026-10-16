#!/bin/bash
# Двойной клик — запускает SEO Workspace и открывает его в браузере.
cd "$(dirname "$0")"
if ! lsof -iTCP:8765 -sTCP:LISTEN >/dev/null 2>&1; then
  python3 app/server.py &
  sleep 1
fi
open "http://127.0.0.1:8765"
wait
