import re
import string

# Utility to clean and normalize input text before tokenization or training

def clean_text(text: str) -> str:
    """
    Apply basic text cleaning:
    - Strip whitespace
    - Lowercase
    - Remove extra spaces
    - Remove unwanted punctuation
    """
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)  # collapse multiple spaces
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def remove_code_blocks(text: str) -> str:
    """
    Remove Markdown-style code blocks (```...```) from the input.
    """
    return re.sub(r"```[\s\S]*?```", "", text)

def remove_urls(text: str) -> str:
    """
    Strip out URLs from the text.
    """
    return re.sub(r"https?://\S+", "", text)

def full_clean(text: str) -> str:
    """
    Combine all cleaning steps into one pass.
    """
    text = remove_code_blocks(text)
    text = remove_urls(text)
    text = clean_text(text)
    return text
