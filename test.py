import ollama
import shutil

list = ollama.list()

print ("list", list)

"""Ollama Bianry 확인"""
try:
    ollama_path = shutil.which("ollama")
    if ollama_path is None:
        print (f"[INFO] ▶ℹ️ OLLAMA 가 설치가 필요합니다. - {ollama_path}")
        # installOllama()
    else :
        print (f"[INFO] ✅ OLLAMA 가 설치되어 있습니다. - {ollama_path}")
except Exception as e:
    print (f"[ERROR] ⛔ OLLAMA 환경 확인 중 오류가 발생했습니다. - {e}")