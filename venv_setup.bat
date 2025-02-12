@echo off
set VENV_DIR=venv

if not exist %VENV_DIR% (
    python -m venv %VENV_DIR%
    call %VENV_DIR%\Scripts\activate
    pip install --upgrade pip
    pip install -r requirements.txt
) else (
    call %VENV_DIR%\Scripts\activate
)

python run.py
