from datasets import Dataset

# Convert list of strings to HF-compatible dataset
def get_training_dataset(texts: list[str], tokenizer):
    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, padding="max_length")

    data = {"text": texts}
    dataset = Dataset.from_dict(data)
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    return tokenized_dataset