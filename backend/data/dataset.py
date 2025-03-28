# Import the HuggingFace datasets interface
from datasets import Dataset

# Convert a list of plain text strings into a HuggingFace-compatible dataset,
# tokenize the entries, and prepare them for model training.
def get_training_dataset(texts: list[str], tokenizer):
    # Inner function to tokenize each example using the provided tokenizer
    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, padding="max_length")

    # Wrap the list of texts into a dictionary for HF Dataset
    data = {"text": texts}

    # Convert raw text list into HuggingFace Dataset format
    dataset = Dataset.from_dict(data)

    # Apply tokenization to the entire dataset in batch mode
    tokenized_dataset = dataset.map(tokenize_function, batched=True)

    # Return the preprocessed dataset
    return tokenized_dataset
