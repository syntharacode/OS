import re

# Simple preprocessing parser for prompts and training texts

def clean_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def extract_code_snippets(text: str) -> list[str]:
    # Finds triple backtick code blocks in markdown style
    return re.findall(r"```[\s\S]*?```", text)


def extract_links(text: str) -> list[str]:
    return re.findall(r"https?://\S+", text)


def is_valid_prompt(text: str) -> bool:
    return len(text.strip()) > 3 and any(c.isalnum() for c in text)