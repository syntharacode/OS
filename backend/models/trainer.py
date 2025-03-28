from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling
from backend.models.loader import load_model
from backend.data.dataset import get_training_dataset
from backend.core.config import settings
from backend.data.cleaner import full_clean  # NEU
import torch

def fine_tune_model(train_texts: list[str]):
    print("[SyntharaOS] Starting fine-tuning...")

    llm = load_model()
    model = llm["model"]
    tokenizer = llm["tokenizer"]

    # CLEAN TRAINING TEXTS
    train_texts = [full_clean(t) for t in train_texts]

    train_dataset = get_training_dataset(train_texts, tokenizer)

    args = TrainingArguments(
        output_dir="outputs",
        overwrite_output_dir=True,
        num_train_epochs=1,
        per_device_train_batch_size=2,
        save_steps=10,
        save_total_limit=2,
        logging_dir="logs",
        logging_steps=5,
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    trainer.train()
    print("[SyntharaOS] Fine-tuning complete.")
    return model
