import requests
import os
from dotenv import load_dotenv

OLLAMA_URL = "http://localhost:11434/"


def apiGenerate(messages, model="mistral", temperature=0.7):
    """Ollama API Generate 호출"""
    url = OLLAMA_URL + "api/generate"
    payload = {
        "model": model,
        "messages": messages,
        "options": {"temperature": temperature},
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()
        return data.get("response", "[ERROR] OLLAMA API : Generate Response (response)")
    except Exception as e:
        print(f"오류 발생: {e}")
        return None

def apiTags () :
    """Ollama API Tags 호출"""
    url  = OLLAMA_URL + "api/tags"
    
    try :
        response = requests.post(url)
        data = response.json()
        return data.get("models", "[ERROR] OLLAMA API : Tags Response (models)")
    except Exception as e: 
        print (f"[ERROR] OLLAMA API : {e}")
        return None