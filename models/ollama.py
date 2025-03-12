import sys
import subprocess
import time
import importlib.util as libutil

# Ollama 확인
def checkOllama():
    """Ollama 확인"""
    try:
        if libutil.find_spec("ollama") is None:
            installOllama()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] ⛔ OLLAMA 패키지 설치에 실패했습니다. - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA 환경 확인중 오류가 발생했습니다. - {e}")
        sys.exit(1)

# Ollama 설치
def installOllama():
    """Ollama 설치"""
    try:
        print(f"[INFO] 📦 OLLAMA 가 설치되어 있지 않습니다. 자동으로 설치합니다.")
        subprocess.run([sys.executable, "-m", "pip", "install", "ollama"], check=True)
    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA 패키지 설치에 실패 했습니다. - {e}")
        sys.exit(1)


def startOllama():
    """Ollama 실행 / 프로세스 반환"""
    try:
        checkOllama()
        process = subprocess.Popen(
            ["ollama", "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        time.sleep(3)
        print(f"[INFO] 🦙 OLLAMA 가 실행 되었습니다.")
        return process
    except Exception as e:
        print(f"[ERROR] OLLAMA : Start Ollama - {e}")
        return None


def stopOllama(process):
    """Ollama 프로세스 종료"""

    if process:
        process.terminate()
        process.wait()
        print("[INFO] OLLAMA : Ollama 서버가 종료되었습니다.")
