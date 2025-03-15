import sys
import subprocess
import time
import importlib.util as libutil
import shutil
import platform
import psutil

OLLAMA_PORT = 11434


# Ollama Binary 확인
def checkOllama():
    """Ollama Bianry 확인"""
    try:
        ollama_path = shutil.which("ollama")
        if ollama_path is None:
            print(f"[INFO] ℹ️ OLLAMA가 설치되어 있지 않습니다. 설치를 진행합니다.")
            installOllama()
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
                f"[INFO] 📦 OLLAMA 가 설치되어 있지 않습니다. {system.capitalize()}에 Ollama를 자동으로 설치합니다."
            )
            try:
                subprocess.run(
                    ["winget", "install", "--id=Ollama.Ollama", "-e"], check=True
                )
            except FileNotFoundError:
                print(
                    "[ERROR] ⛔ Winget이 설치되어 있지 않습니다. 수동으로 Ollama를 설치하세요. https://ollama.com"
                )
                sys.exit(1)
            except Exception as e:
                print(
                    f"[ERROR] ⛔ {system.capitalize()}에 Ollama를 설치하는 중 예상치 못한 오류가 발생했습니다. - {e}"
                )
        elif system in ["linux", "darwin"]:
            print(
                f"[INFO] 📦 OLLAMA 가 설치되어 있지 않습니다. {system.capitalize()} Ollama를 자동으로 설치합니다."
            )
            subprocess.run(
                # ["curl", "-fsSL", "https://ollama.com/install.sh", "|", "sh"],
                ["curl -fsSL https://ollama.com/install.sh | sh"],
                check=True,
                shell=True,
            )
        else:
            print(f"[ERROR] ⛔ 지원하지 않는 운영 체제 - {system.capitalize()}")
            sys.exit(1)

        print(f"[INFO] ✅ OLLAMA 설치에 성공했습니다. - {system.capitalize()}")

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] ⛔ OLLAMA 설치 실패 - {e}")
        sys.exit(1)

    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA : Install Ollama - {e}")
        sys.exit(1)


def checkProcessPort():
    """Ollama Process 확인"""
    system = platform.system().lower()

    try:
        if system == "windows":
            result_netstat = subprocess.run(
                ["netstat", "-ano"], capture_output=True, text=True
            )
            pid = None
            for line in result_netstat.stdout.splitlines():
                if f":{OLLAMA_PORT}" in line:
                    parts = line.split()
                    pid = parts[-1]
                    break
            if not pid:
                return None

            result_tasklist = subprocess.run(
                ["tasklist", "/FI", f"PID eq {pid}"], capture_output=True, text=True
            )
            for line in result_tasklist.stdout.splitlines():
                if "ollama.exe" in line.lower():
                    return int(pid)

            return None

        elif system in ["linux", "darwin"]:
            result_netstat = subprocess.run(
                ["netstat", "-tulnp"], capture_output=True, text=True
            )
            pid = None
            for line in result_netstat.stdout.splitlines():
                if f":{OLLAMA_PORT}" in line:
                    parts = line.split()
                    pid = parts[-1].split("/")[0]
                    break

            if not pid:
                return None

            result_ps = subprocess.run(
                ["ps", "-p", pid, "-o", "comm="], capture_output=True, text=True
            )
            process_name = result_ps.stdout.strip()
            if process_name == "ollama":
                return int(pid)

            return None

        else:
            print(f"[ERROR] ⛔ 지원하지 않는 운영체제 - {system.capitalize()}")
            return None

    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA 프로세스 확인 중 오류 발생 - {e}")
        return None


def startOllama():
    """Ollama 실행 / 프로세스 반환"""
    try:
        # Ollama 설치 확인
        checkOllama()
        # Ollama 실행 확인
        existing_pid = checkProcessPort()

        # Ollama 실행
        if existing_pid:
            print(f"[INFO] ℹ️ Ollama가 이미 실행 중입니다. PID : {existing_pid}")
            return psutil.Process(existing_pid)
            # try:
            #     existing_process = psutil.Process(existing_pid)
            #     process = subprocess.Popen(
            #         ["ollama", "serve"],
            #         stdout=subprocess.PIPE,
            #         stderr=subprocess.PIPE,
            #         text=True,
            #         preexec_fn=lambda: existing_process,
            #     )
            # except psutil.NoSuchProcess:
            #     print(f"[ERROR] ⛔ 기존 OLLAMA 프로세스를 찾을 수 없습니다.")
            #     return None
        else:
            process = subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            time.sleep(3)
            if process.poll() is not None:
                stderr_output = process.stderr.read()
                print(f"[ERROR] ⛔ OLLAMA 실행 오류 - {stderr_output}")
                return None

        print(f"[TEST] ☑️ startOllama - {process}")
        print(f"[INFO] 🦙 OLLAMA 프로세스가 실행 되었습니다. PID : {process.pid}")
        return process

    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA : Start Ollama - {e}")
        return None


def stopOllama(process):
    """Ollama 프로세스 종료"""
    try:
        pid = checkProcessPort()
        if pid:
            process = psutil.Process(pid)
            process.terminate()
            process.wait()
            print(f"[INFO] ✅ OLLAMA가 종료되었습니다. PID : {pid}")
        else:
            print(f"[INFO] ℹ️ 실행 중인 OLLAMA 프로세스가 없습니다.")
        # if process:
        #     process.terminate()
        #     process.wait()
        #     print(f"[INFO] OLLAMA : Ollama 서버가 종료되었습니다. - {process}")
        # else:
        #     print(f"[INFO] ℹ️ OLLAMA 가 실해중이 아닙니다. - {process}")
    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA 종료 오류 - {e}")
