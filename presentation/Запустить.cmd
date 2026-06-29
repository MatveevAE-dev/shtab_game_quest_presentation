@echo off
rem ── Запуск презентации на локальном сервере (pdf.js требует http, не file://) ──
chcp 65001 >nul
cd /d "%~dp0.."
echo Открываю http://localhost:8755/presentation/index.html
start "" http://localhost:8755/presentation/index.html
python -m http.server 8755
