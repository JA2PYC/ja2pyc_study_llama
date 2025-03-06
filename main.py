import os
import sys
import subprocess

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

    ollamaProcess = ollama.startOllama()

    try:
        if ollamaProcess:
            print("[INFO] Ollama 서버가 실행 되었습니다.")
    except Exception as e:
        print(f"[ERROR] Run Ollama : Ollama 서버 실행중 오류 발생 - {e}")
    finally:
        ollama.stopOllama(ollamaProcess)


# Run Flask
def run_flask():
    """Flask 애플리케이션 실행"""
    
    global FLASK_PROCESS
    app_path = os.path.join(DASHBOARD_PATH, "app.py")
    
    if not os.path.exists(app_path):
        print(f"❌ {app_path} 파일이 존재하지 않습니다.")
        return
    
    print("[INFO] 🚀 Flask 서버 실행 중...")
    print(f"[TEST] Main PID: {os.getpid()}")
    print("[TEST] main.py run_flask / sys.path : ", sys.path)
    subprocess.run([PYTHON_EXEC, "-m", "dashboard.app"])


# TEST Sys path
# print("[TEST] main.py / sys.path : ", sys.path)

# Initialize
if __name__ == "__main__":
    activate_virtualenv()  # 가상환경 활성화
    install_requirements()  # 의존성 설치
    print(f"Main Python Executable: {sys.executable}")
    print(f"Main Virtual Environment: {sys.prefix}")
    print(f"Main PID: {os.getpid()}")
    run_ollama()
    run_flask()  # Flask 실행

# import os
# import sys
# import subprocess


# print("Main", sys.executable)

# def create_virtualenv():
#     """Create a virtual environment if it doesn't exist."""
#     if not os.path.exists("venv"):
#         print("Creating a virtual environment...")
#         try:
#             subprocess.run(["python", "-m", "venv", "venv"], check=True)
#             print("Successfully created virtual environment.")
#         except subprocess.CalledProcessError as e:
#             print(f"Failed to create a virtual environment: {e}")
#             sys.exit(1)


# def activate_virtualenv():
#     """Ensure the script runs inside the virtual environment."""
#     venv_python = os.path.join(
#         "venv", "Scripts" if os.name == "nt" else "bin", "python"
#     )
#     print("VENV", sys.executable)
#     if sys.executable != os.path.abspath(venv_python):
#         print("Restarting script inside the virtual environment...")
#         print("Subprocess", sys.executable)
#         subprocess.run([venv_python] + sys.argv)
#         # sys.exit(0)


# def install_dependencies():
#     """Install dependencies from requirements.txt."""
#     requirements_file = "requirements.txt"
#     if not os.path.exists(requirements_file) or os.path.getsize(requirements_file) == 0:
#         print(
#             "Skipping dependency installation (no requirements.txt or file is empty)."
#         )
#         return

#     print("Installing dependencies...")
#     try:
#         subprocess.run(
#             [sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True
#         )
#         subprocess.run(
#             [sys.executable, "-m", "pip", "install", "-r", requirements_file],
#             check=True,
#         )
#         print("Dependencies installed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to install dependencies: {e}")
#         sys.exit(1)


# def run_flask_app():
#     """Run the Flask application."""
#     try:
#         from dashboard import create_app

#         print("Creating Flask app...")
#         app = create_app()
#         app.run(debug=True)
#     except ImportError as e:
#         print(f"Flask App Import Error: {e}")
#         sys.exit(1)
#     except Exception as e:
#         print(f"Flask App Exception: {e}")
#         sys.exit(1)


# def main():
#     create_virtualenv()
#     print("Create", sys.executable)
#     activate_virtualenv()
#     print("Activate", sys.executable)
#     install_dependencies()
#     run_flask_app()


# if __name__ == "__main__":
#     if "FLASK_RUN_FROM_CLI" not in os.environ:
#         main()

# # import os
# # import sys
# # import subprocess

# # # Create Virtual Environment.
# # def create_virtualenv():
# #     """Create a virtual environment."""
# #     if not os.path.exists("venv"):
# #         print("Creating a virtual environment...")
# #         try:
# #             subprocess.run(["python", "-m", "venv", "venv"], check=True)
# #             print("Successfully created virtual environment.")
# #         except subprocess.CalledProcessError as e:
# #             print(f"Failed to create a virtual environment : {e}")
# #             sys.exit(1)
# #         except Exception as e:
# #             print(f"Failed to create a virtual environment : {e}")
# #             sys.exit(1)


# # def activate_virtualenv():
# #     """Activate a virtual environment."""
# #     if os.environ.get("VIRTUAL_ENV"):
# #         print("Virtual environment is already activated.")
# #         return

# #     venv_python = os.path.join(
# #         "venv", "Scripts" if os.name == "nt" else "bin", "python"
# #     )
# #     activate_script = os.path.join(
# #         "venv", "Scripts" if os.name == "nt" else "bin", "activate"
# #     )
# #     if not os.path.exists(activate_script):
# #         print("Cannot find a venv script.")
# #         sys.exit(1)

# #     if sys.executable != os.path.abspath(venv_python):
# #         os.environ["VIRTUAL_ENV"] = os.path.abspath("venv")
# #         os.environ["PATH"] = os.path.join("venv", "bin") + os.pathsep + os.environ["PATH"]
# #         print("Restart script inside the virtual environment.")
# #         os.execv(venv_python, [venv_python] + sys.argv)
# #     print("Activate a virtual environment.")


# # def install_dependencies():
# #     """Install Dependencies.."""
# #     if os.environ.get("DEPENDENCIES_CHECKED"):
# #         print("Already checked dependencies.")
# #         return
# #     requirements_file = "requirements.txt"
# #     if not os.path.exists(requirements_file):
# #         print("Cannot find a requirements.txt. Skip install dependenceis.")
# #         return

# #     if os.path.getsize(requirements_file) == 0:
# #         print("File is empty. Skip install dependencies.")
# #         return

# #     print("Install dependencies.")
# #     try:
# #         subprocess.check_call(
# #             [sys.executable, "-m", "pip", "install", "--upgrade", "pip"]
# #         )
# #         subprocess.check_call(
# #             [sys.executable, "-m", "pip", "install", "-r", requirements_file]
# #         )
# #         os.environ["DEPENDENCIES_CHECKED"] = "true"
# #         print("Complete install dependencies.")
# #     except Exception as e:
# #         print(f"Failed to install dependencies : {e}")
# #         sys.exit(1)


# # def run_flask_app():
# #     """Run main"""
# #     try:
# #         from dashboard import create_app

# #         print("Create flask app")
# #         app = create_app()

# #         app.run(debug=True)
# #     except ImportError as e:
# #         print(f"Flask App Import Error : {e}")
# #         sys.exit(1)
# #     except Exception as e:
# #         print(f"Flask App Exception : {e}")
# #         sys.exit(1)


# # def main():
# #     create_virtualenv()
# #     activate_virtualenv()
# #     install_dependencies()
# #     run_flask_app()


# # if __name__ == "__main__":
# #     if "FLASK_RUN_FROM_CLI" not in os.environ:
# #         main()
