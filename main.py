import os
import sys
import subprocess
import time

# VENV Settings
VENV_PATH = os.path.join(os.path.dirname(__file__), "venv")
PYTHON_EXEC = (
    os.path.join(VENV_PATH, "Scripts", "python.exe")
    if os.name == "nt"
    else os.path.join(VENV_PATH, "bin", "python")
)
REQUIREMENTS_FILE = "requirements.txt"

# PATH
DASHBOARD_PATH = os.path.join(os.path.dirname(__file__), "dashboard")

# PROCESS
OLLAMA_PROCESS = None
FLASK_PROCESS = None


# Create VENV
def create_virtualenv():
    """가상환경이 없으면 생성"""
    if not os.path.exists(VENV_PATH):
        print("[INFO] ⚙️ 가상환경을 생성하는 중...")
        subprocess.run([sys.executable, "-m", "venv", VENV_PATH], check=True)


# Activate VENV
def activate_virtualenv():
    """가상환경이 활성화되지 않으면 재실행"""
    if sys.prefix == sys.base_prefix:
        if os.environ.get("VIRTUAL_ENV_ACTIVE"):
            print("[INFO] 🚨 가상환경 중복 실행 방지 : 실행 중단")
            sys.exit(1)
        os.environ["VIRTUAL_ENV_ACTIVE"] = "1"
        print("[INFO] 🔍 가상환경이 감지되지 않았습니다. 자동으로 실행합니다.")
        create_virtualenv()
        print(f"[INFO] 🚀 가상환경에서 다시 실행: {PYTHON_EXEC} {sys.argv}")
        subprocess.run([PYTHON_EXEC] + sys.argv)
        sys.exit()


# Install VENV
def install_requirements():
    """필요한 패키지를 설치"""
    print("[INFO] 📦 패키지 설치 중...")
    if os.path.exists(REQUIREMENTS_FILE):
        subprocess.run(
            [PYTHON_EXEC, "-m", "pip", "install", "-r", REQUIREMENTS_FILE], check=True
        )
    else:
        subprocess.run([PYTHON_EXEC, "-m", "pip", "install", "flask"], check=True)


# Run Ollama
def run_ollama():
    """Ollama Server 실행"""
    global OLLAMA_PROCESS
    from models import ollama

    if OLLAMA_PROCESS is None:
        try:
            OLLAMA_PROCESS = ollama.startOllama()
            time.sleep(3)
        except Exception as e:
            print(f"[ERROR] Ollama 서버 실행중 오류 발생 : {e}")
        finally:
            print(f"[TEST] Ollama - {OLLAMA_PROCESS}")
            if OLLAMA_PROCESS:
                print("[INFO] 🦙 Ollama 서버가 실행 되었습니다.")
            else:
                print("[ERROR] ⛔ Ollama 서버 실행에 실패했습니다.")
                OLLAMA_PROCESS = None


# Run Flask
def run_flask():
    """Flask 애플리케이션 실행"""

    global FLASK_PROCESS
    app_path = os.path.join(DASHBOARD_PATH, "app.py")

    if not os.path.exists(app_path):
        print(f"❌ {app_path} 파일이 존재하지 않습니다.")
        return

    print("[INFO] 🚀 Flask 서버 실행 중...")
    # print(f"[TEST] Main PID: {os.getpid()}")
    # print("[TEST] main.py run_flask / sys.path : ", sys.path)
    # subprocess.run([PYTHON_EXEC, "-m", "dashboard.app"])
    FLASK_PROCESS = subprocess.Popen([PYTHON_EXEC, "-m", "dashboard.app"])


# Close Process
def cleanup():
    global OLLAMA_PROCESS, FLASK_PROCESS

    if FLASK_PROCESS:
        print("[INFO] 🛑 Flask 서버 종료중...")
        FLASK_PROCESS.terminate()
        FLASK_PROCESS.wait()
        print("[INFO] Flask 서버가 종료되었습니다.")

    if OLLAMA_PROCESS:
        print("[INFO] 🛑 Ollama 서버 종료중...")
        from models import ollama

        ollama.stopOllama(OLLAMA_PROCESS)
        OLLAMA_PROCESS = None
        print("[INFO] Ollama 서버가 종료되었습니다.")


# TEST Sys path
# print("[TEST] main.py / sys.path : ", sys.path)

# Initialize
if __name__ == "__main__":
    # Append File Path
    sys.path.append(os.path.dirname(__file__))
    try:
        activate_virtualenv()  # 가상환경 활성화
        install_requirements()  # 의존성 설치
        # print(f"[TEST] Main Python Executable: {sys.executable}")
        # print(f"[TEST] Main Virtual Environment: {sys.prefix}")
        # print(f"[TEST] Main PID: {os.getpid()}")
        run_ollama()
        run_flask()  # Flask 실행

        while True:
            time.sleep(5)
    except KeyboardInterrupt as k:
        print(f"[INFO] 🛑 종료 요청 감지! 정리 중... : {k}")

    except Exception as e:
        print(f"[ERROR] 예외 발생 : {e}")

    finally:
        cleanup()
