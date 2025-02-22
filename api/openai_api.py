import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()
print(OPENAI_API_KEY)

def chatCompletion(messages, model="gpt-4", temperature=0.7):
    """ChatGPT API 호출"""
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API KEY가 설정되지 않았습니다.")

    response = client.chat.completions.create(
        model=model, message=messages, temperature=temperature
    )
    print(response)
    return response["choices"][0]["message"]["content"]