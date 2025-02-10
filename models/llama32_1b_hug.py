import transformers
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# 모델과 토크나이저 설정
model_name = "meta-llama/Llama-3.2-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 모델 불러오기
model = transformers.AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

# pad_token_id 설정: eos_token_id가 None일 경우 동일하게 설정
if model.config.pad_token_id is None:
    model.config.pad_token_id = tokenizer.eos_token_id

# 텍스트 생성 파이프라인 설정
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    device_map="auto"
)

# 텍스트 생성
sequences = pipeline(
    'I have chicken, tomato sauce, cheese at home. What can I cook for dinner?\n',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    truncation=True,
    max_length=400,
)

# 결과 출력
for seq in sequences:
    print(f"Result: {seq['generated_text']}")


# import transformers
# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM

# model_name = "meta-llama/Llama-3.2-1B"
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# model = transformers.AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)


# # pad_token_id 설정: eos_token_id가 None일 경우 동일하게 설정
# if model.config.pad_token_id is None:
#     model.config.pad_token_id = tokenizer.eos_token_id

# pipeline = transformers.pipeline(
#     "text-generation",
#     model = model,
#     tokenizer=tokenizer,
#     torch_dtype=torch.float16,
#     device_map="auto"
# )

# sequences = pipeline(
#     'I have chicken, tomatos sauce, cheese at home. What can I cook for dinner?\n',
#     do_sample = True,
#     top_k = 10,
#     num_return_sequences = 1,
#     eos_token_id = tokenizer.eos_token_id,
#     truncation = True,
#     max_length = 400,
# )

# for seq in sequences:
#     print(f"Result: {seq['generated_text']}")