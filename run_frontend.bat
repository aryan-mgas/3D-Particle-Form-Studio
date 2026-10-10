@echo off
cd /d "%~dp0"
echo Starting local web server...
echo Open http://localhost:8000/frontend/ in Chrome or Edge
python -m http.server 8000
pause
