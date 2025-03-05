import requests
import os
from dotenv import load_dotenv

# OLLAMA API URL
OLLAMA_URL = "http://localhost:11434/"


# Generate Chat
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
        print(f"[ERROR] OLLAMA API : Generate - {e}")
        return None


# Models List
def apiTags():
    """Ollama API Tags 호출"""
    url = OLLAMA_URL + "api/tags"

    try:
        response = requests.post(url)
        data = response.json()
        return data.get("models", "[ERROR] OLLAMA API : Tags Response (models)")
    except Exception as e:
        print(f"[ERROR] OLLAMA API : Tags - {e}")
        return None


# Pull Model
def apiPull(model):
    url = OLLAMA_URL + "api/pull"
    payload = {"name": model}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("status", "[ERROR] OLLAMA API : Pull Response (status)")
    except Exception as e:
        print(f"[ERROR] OLLAMA API : Pull - {e}")
        return None


#  Delete Model
def apiDelete(model):
    """Ollama API 모델 삭제"""
    url = OLLAMA_URL + "api/delete"
    payload = {"name": model}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("status", "[ERROR] OLLAMA API : Delete Response (status)")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] OLLAMA API : Delete 요청 실패 - {e}")
        return None


# Model Info
def apiShow(model):
    """Ollama API 모델 정보 조회"""
    url = OLLAMA_URL + "api/show"
    payload = {"name": model}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] OLLAMA API : Show 요청 실패 - {e}")
        return None


# Cancel API
def apiCancel():
    """Ollama API 요청 취소"""
    url = OLLAMA_URL + "api/cancel"

    try:
        response = requests.post(url)
        response.raise_for_status()
        return "[SUCCESS] OLLAMA API : 요청이 성공적으로 취소되었습니다."
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] OLLAMA API : Cancel 요청 실패 - {e}")
        return None
