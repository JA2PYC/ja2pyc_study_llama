import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

# 모델 경로 지정
model_path = "C:\\Users\\gr2na\\.llama\\checkpoints\\Llama3.2-1B-Instruct"

# 토크나이저와 모델 로드
tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(model_path)

# GPU를 사용할 수 있다면 모델을 GPU로 이동
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

# 입력 텍스트
prompt = "안녕하세요! LLaMA 모델이 잘 작동하는지 확인해 보겠습니다."

# 토큰화 및 입력 ID 생성
inputs = tokenizer(prompt, return_tensors="pt").to(device)

# 모델 추론
with torch.no_grad():
    outputs = model.generate(**inputs, max_length=100)

# 출력 디코딩
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("LLaMA 모델의 응답:", response)
