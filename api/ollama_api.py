import requests
import os
from dotenv import load_dotenv

OLLAMA_URL = "http://localhost:11434/api/generate"


def chatCompletion(messages, model="mistral", temperature=0.7):
    """Ollama API 호출"""
    url = OLLAMA_URL
    payload = {
        "model": model,
        "messages": messages,
        "options": {"temperature": temperature},
    }

    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        return response_data.get("response", "오류발생")
    except Exception as e:
        print(f"오류 발생: {e}")
        return None
