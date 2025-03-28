# Import HuggingFace training components
from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling

# Load pre-initialized model and tokenizer
from backend.models.loader import load_model

# Get tokenized and prepared training dataset
from backend.data.dataset import get_training_dataset

# Load SyntharaOS configuration (e.g., model settings)
from backend.core.config import settings

# Import PyTorch for tensor handling (used internally by transformers)
import torch

# Fine-tune the currently loaded language model on a list of training texts
def fine_tune_model(train_texts: list[str]):
    print("[SyntharaOS] Starting fine-tuning...")

    # Load model and tokenizer from Synthara engine
    llm = load_model()
    model = llm["model"]
    tokenizer = llm["tokenizer"]

    # Prepare dataset for training
    train_dataset = get_training_dataset(train_texts, tokenizer)

    # Define training arguments for the HuggingFace Trainer
    args = TrainingArguments(
        output_dir="outputs",              # Directory to save model checkpoints
        overwrite_output_dir=True,         # Overwrite previous checkpoints
        num_train_epochs=1,                # Number of full passes over the training data
        per_device_train_batch_size=2,     # Training batch size per device (GPU/CPU)
        save_steps=10,                     # Save model every 10 steps
        save_total_limit=2,                # Keep only the 2 most recent checkpoints
        logging_dir="logs",                # Log directory for TensorBoard
        logging_steps=5                    # Log training metrics every 5 steps
    )

    # Define data collator for language modeling (no masked LM)
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False
    )

    # Initialize HuggingFace Trainer with model, config, and data
    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    # Begin fine-tuning
    trainer.train()

    print("[SyntharaOS] Fine-tuning complete.")
    return model
