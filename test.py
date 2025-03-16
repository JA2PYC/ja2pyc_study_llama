# Ollama Process 테스트 코드
from models import ollama
print("[TEST] ☑️ 프로세스 실행 테스트")

process = ollama.startOllama()
print(f"Ollama 실행 프로세스 : {process}")

print("[TEST] ☑️ 프로세스 종료 테스트")

ollama.stopOllama()

print("[TEST] ☑️ 프로세스 중복 테스트")
process1 = ollama.startOllama()
process2 = ollama.startOllama()
print(f"프로세스 1 PID : {process1.pid}")
print(f"프로세스 2 PID : {process2.pid}")

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