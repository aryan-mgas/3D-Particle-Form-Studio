@echo off
cd /d "%~dp0backend"
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8001
pause
