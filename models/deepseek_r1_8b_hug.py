from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model

model_name = "deepseek-ai/deepseek-mistral-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

lora_config = LoraConfig(
    r=8, lora_alpha=32, target_modules=["q_proj", "v_proj"], lora_dropout=0.1
)
model = get_peft_model(model, lora_config)

training_args = TrainingArguments(
    output_dir="./deepseek-finetuned",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-5,
    num_train_epochs=3,
    save_steps=500,
    save_total_limit=2
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data
)

trainer.train()
