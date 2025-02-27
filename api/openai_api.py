import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)
# openai = OpenAI()

# 사용 가능한 모델 리스트 가져오기
def getModelsList():
    models = openai.models.list()
    return [model.id for model in models.data]

# LLM 채팅
def chatCompletion(messages, model="gpt-4", temperature=0.7):
    """ChatGPT API 호출"""
    print(messages)
    print(model)
    print(temperature)
    
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API KEY가 설정되지 않았습니다.")
    
    try:
        response = openai.chat.completions.create(
            model=model, messages=messages, temperature=temperature
        )
        print(response)
        # return response["choices"][0]["message"]["content"]
        return response.choices[0].message.content
    except Exception as e:
        print(f"오류 발생: {e}")
        return None
    
