#!/bin/bash

# 가상 환경 디렉토리 설정
VENV_DIR="venv"

# 가상 환경이 없으면 생성
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    pip install --upgrade pip
    pip install -r requirements.txt
else
    source "$VENV_DIR/bin/activate"
fi

# Flask 앱 실행
python run.py
