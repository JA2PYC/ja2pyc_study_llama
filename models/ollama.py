import sys
import subprocess
import time
import importlib.util as libutil
import shutil
import platform


# Ollama Binary 확인
def checkOllama():
    """Ollama Bianry 확인"""
    try:
        ollama_path = shutil.which("ollama")
        if ollama_path is None:
            print(f"[INFO] ℹ️ℹ OLLAMA 설치를 진행합니다. - {ollama_path}")
            # installOllama()
        else:
            print(f"[INFO] ✅ OLLAMA 가 설치되어 있습니다. - {ollama_path}")
    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA 환경 확인 중 오류가 발생했습니다. - {e}")


def installOllama():
    """Ollama Binary 설치"""
    try:
        system = platform.system().lower()

        if system == "windows":
            print(
                f"[INFO] 📦 OLLAMA 가 설치되어 있지 않습니다. {system.capitalize()} Ollama를 자동으로 설치합니다."
            )
            subprocess.run(
                ["widget", "install", "--id=Ollama.Ollama", "-e"], check=True
            )
        elif system in ["linux", "darwin"]:
            print(
                f"[INFO] 📦 OLLAMA 가 설치되어 있지 않습니다. {system.capitalize()} Ollama를 자동으로 설치합니다."
            )
            subprocess.run(
                ["curl", "-fsSL", "https://ollama.com/install.sh", "|", "sh"],
                check=True,
                shell=True,
            )
        else:
            print(f"[ERROR] ⛔ 지원하지 않는 운영 체제 - {system.capitalize()}")
            sys.exit(1)

        print(f"[INFO] ✅ OLLAMA 설치에 성공했습니다. - {system.capitalize()}")

    except Exception as e:
        print(f"[ERROR] OLLAMA : Install Ollama - {e}")
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
