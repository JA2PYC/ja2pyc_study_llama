# ------------------------------
# 경로 모듈 테스트
import os
import sys

print("=== 경로 정보 출력 ===")
print(f"os.getcwd():       {os.getcwd()}")
print(f"__file__:           {__file__}")
print(f"os.path.dirname:   {os.path.dirname(__file__)}")
print(f"sys.path[0]:        {sys.path[0]}")
print("=====================")

# try:
#     from config import testmodule
#     testmodule.test_module()
# except Exception as e:
#     print("[TEST] ☑️ Import Error:", e)

# ------------------------------
# # 경로 설정 테스트
# import os
# import sys

# PROJECT_ROOT = os.getcwd()  # 현재 실행 위치를 기준으로 경로 설정
# LOG_DIR = os.path.join(PROJECT_ROOT, "log")
# print(PROJECT_ROOT)
# print(LOG_DIR)

# PROJECT_ROOT = os.path.abspath(sys.path[0])
# LOG_DIR = os.path.join(PROJECT_ROOT, "log")

# print(PROJECT_ROOT)
# print(LOG_DIR)

# ------------------------------
# # Ollama Process 테스트 코드
# from models import ollama
# print("[TEST] ☑️ 프로세스 실행 테스트")

# process = ollama.startOllama()
# print(f"Ollama 실행 프로세스 : {process}")

# print("[TEST] ☑️ 프로세스 종료 테스트")

# ollama.stopOllama()

# print("[TEST] ☑️ 프로세스 중복 테스트")
# process1 = ollama.startOllama()
# process2 = ollama.startOllama()
# print(f"프로세스 1 PID : {process1.pid}")
# print(f"프로세스 2 PID : {process2.pid}")

# ------------------------------
# Ollama Binary 테스트 코드
# import ollama
# import shutil

# list = ollama.list()

# print ("list", list)

# """Ollama Bianry 확인"""
# try:
#     ollama_path = shutil.which("ollama")
#     if ollama_path is None:
#         print (f"[INFO] ▶ℹ️ OLLAMA 가 설치가 필요합니다. - {ollama_path}")
#         # installOllama()
#     else :
#         print (f"[INFO] ✅ OLLAMA 가 설치되어 있습니다. - {ollama_path}")
# except Exception as e:
#     print (f"[ERROR] ⛔ OLLAMA 환경 확인 중 오류가 발생했습니다. - {e}")