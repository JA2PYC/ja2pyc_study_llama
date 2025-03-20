import sys
import subprocess
import time
import importlib.util as libutil
import shutil
import platform
import psutil

OLLAMA_PORT = 11434
MAX_WAIT_TIME = 10


# OLLAMA 설치 확인
def checkOllama():
    """Ollama Bianry 확인"""
    try:
        subprocess.run(
            ["ollama", "--version"], capture_output=True, check=True, text=True
        )
        print(f"[INFO] ✅ OLLAMA가 설치되어 있습니다.")
        return True
    except FileNotFoundError:
        print(f"[INFO] ℹ️ OLLAMA가 설치되어 있지 않습니다. 설치를 진행합니다.")
        response = installOllama()
        return response
    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA 환경 확인 중 오류 발생 - {e}")
        return False

    # try:
    #     ollama_path = shutil.which("ollama")
    #     if ollama_path is None:
    #         print(f"[INFO] ℹ️ OLLAMA가 설치되어 있지 않습니다. 설치를 진행합니다.")
    #         installOllama()
    #     else:
    #         print(f"[INFO] ✅ OLLAMA 가 설치되어 있습니다. - {ollama_path}")
    # except Exception as e:
    #     print(f"[ERROR] ⛔ OLLAMA 환경 확인 중 오류 발생 - {e}")


# OLLAMA 설치
def installOllama():
    """Ollama Binary 설치"""
    try:
        system = platform.system().lower()

        if system == "windows":
            print(
                f"[INFO] 📦 OLLAMA 가 설치되어 있지 않습니다. {system.capitalize()}에 OLLAMA를 설치합니다."
            )
            subprocess.run(
                ["winget", "install", "--id=Ollama.Ollama", "-e"], check=True
            )
        elif system in ["linux", "darwin"]:
            print(
                f"[INFO] 📦 OLLAMA 가 설치되어 있지 않습니다. {system.capitalize()} OLLAMA를 설치합니다."
            )
            subprocess.run(
                # ["curl", "-fsSL", "https://ollama.com/install.sh", "|", "sh"],
                "curl -fsSL https://ollama.com/install.sh | sh",
                check=True,
                shell=True,
            )
        else:
            print(f"[ERROR] ⛔ 지원하지 않는 운영 체제 - {system.capitalize()}")
            return False

        print(f"[INFO] ✅ OLLAMA 설치에 성공했습니다. - {system.capitalize()}")
        return True

    except FileNotFoundError:
        print(
            "[ERROR] ⛔ 자동 설치를 진행할 수 없습니다. 수동으로 Ollama를 설치하세요. https://ollama.com"
        )
        return False
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] ⛔ OLLAMA 설치 실패 - {e}")
        return False
    except Exception as e:
        print(
            f"[ERROR] ⛔ {system.capitalize()}에 OLLAMA 설치 중 오류가 발생했습니다. - {e}"
        )
        return False


# OLLAMA 실행 확인
def checkProcessPort():
    """Ollama Process 확인"""
    try:
        for process in psutil.process_iter(attrs=["pid", "name"]):
            # print(f"[TEST] ☑️ checkProcessPort - {process}")
            if "ollama" in str(process.info["name"]).lower():
                for conn in process.net_connections(kind="inet"):
                    if conn.laddr.port == OLLAMA_PORT:
                        print(
                            f"[INFO] ℹ️ OLLAMA 프로세스를 확인했습니다. PID : {process.info['pid']}"
                        )
                        return int(process.info["pid"])

    except (psutil.AccessDenied, psutil.NoSuchProcess, TypeError) as e:
        print(f"[ERROR] ⛔ OLLAMA 프로세스 확인 중 오류 발생 - {e}")
        return None
    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA 프프르세스 확인 중 오류 발생 - {e}")
        return None

    # system = platform.system().lower()

    # try:
    #     if system == "windows":
    #         result_netstat = subprocess.run(
    #             ["netstat", "-ano"], capture_output=True, text=True
    #         )
    #         pid = None
    #         for line in result_netstat.stdout.splitlines():
    #             if f":{OLLAMA_PORT}" in line:
    #                 parts = line.split()
    #                 pid = parts[-1]
    #                 break
    #         if not pid:
    #             return None

    #         result_tasklist = subprocess.run(
    #             ["tasklist", "/FI", f"PID eq {pid}"], capture_output=True, text=True
    #         )
    #         for line in result_tasklist.stdout.splitlines():
    #             if "ollama.exe" in line.lower():
    #                 return int(pid)

    #         return None

    #     elif system in ["linux", "darwin"]:
    #         result_netstat = subprocess.run(
    #             ["netstat", "-tulnp"], capture_output=True, text=True
    #         )
    #         pid = None
    #         for line in result_netstat.stdout.splitlines():
    #             if f":{OLLAMA_PORT}" in line:
    #                 parts = line.split()
    #                 pid = parts[-1].split("/")[0]
    #                 break

    #         if not pid:
    #             return None

    #         result_ps = subprocess.run(
    #             ["ps", "-p", pid, "-o", "comm="], capture_output=True, text=True
    #         )
    #         process_name = result_ps.stdout.strip()
    #         if process_name == "ollama":
    #             return int(pid)

    #         return None

    #     else:
    #         print(f"[ERROR] ⛔ 지원하지 않는 운영체제 - {system.capitalize()}")
    #         return None

    # except Exception as e:
    #     print(f"[ERROR] ⛔ OLLAMA 프로세스 확인 중 오류 발생 - {e}")
    #     return None


# OLLAMA 실행
def startOllama():
    """Ollama 실행 / 프로세스 반환"""
    try:
        # Ollama 설치 확인
        check_result = checkOllama()

        if check_result == False:
            return False

        # Ollama 실행 확인
        existing_pid = checkProcessPort()

        # Ollama 실행
        if existing_pid:
            print(f"[INFO] ℹ️ OLLAMA가 이미 실행 중입니다. PID : {existing_pid}")
            return existing_pid

        try:
            process = subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            # time.sleep(3)
            start_time = time.time()

            while time.time() - start_time < MAX_WAIT_TIME:
                time.sleep(1)

                new_pid = checkProcessPort()

                if new_pid:
                    if process.poll() is not None:
                        stderr_output = process.stderr.read()
                        print(f"[ERROR] ⛔ OLLAMA 실행 오류 - {stderr_output}")
                        return None
                    print(f"[INFO] ✅ OLLAMA 실행 완료. PID : {new_pid}")
                    return new_pid

        except Exception as e:
            print(f"[ERROR] ⛔ OLLAMA 프로세스 실행 중 오류 발생 - {e}")
            return False

        # print(f"[TEST] ☑️ startOllama - {process}")

        # new_pid = checkProcessPort()

        # if new_pid:
        #     print(f"[INFO] 🦙 OLLAMA 프로세스가 실행 되었습니다. PID : {process.pid}")
        #     return new_pid

        # else:
        #     print(f"[ERROR] ⛔ OLLAMA 프로세스 실행 실패 - {new_pid}")
        #     return None

    except Exception as e:
        print(f"[ERROR] ⛔ OLLAMA 실행 중 오류 발생 - {e}")
        return None


def stopOllama():
    """Ollama 프로세스 종료"""
    try:
        pid = checkProcessPort()
        if pid:
            try:
                process = psutil.Process(pid)
                process.terminate()
                process.wait()
                print(f"[INFO] ✅ OLLAMA가 종료되었습니다. PID : {pid}")
            except psutil.NoSuchProcess:
                print(f"[INFO] ℹ️ 이미 종료된 프로세스 입니다.")
            except Exception as e:
                print(f"[ERROR] ⛔ 프로세스 종료 중 오류 발생 - {e}")
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
