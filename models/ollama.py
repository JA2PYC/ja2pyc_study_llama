import subprocess
import time

def startOllama():
    """Ollama실행 프로세스 반환"""
    try:
        process = subprocess.Popen(["ollama", "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(3)
        return process
    except Exception as e:
        print (f"[ERROR] OLLAMA : Start Ollama - {e}")
        return None

def stopOllama(process):
    """Ollama 프로세스 종료"""
    
    if process:
        process.terminate()
        process.wait()
        print("[INFO] OLLAMA : Ollama 서버가 종료되었습니다.")
        
