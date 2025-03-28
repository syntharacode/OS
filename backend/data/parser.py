# Import regular expression module for text parsing
import re

# Simple preprocessing parser for prompts and training texts
# Used during ingestion, validation, and cleaning stages

# Clean up whitespace and normalize spacing
def clean_text(text: str) -> str:
    text = text.strip()  # Remove leading/trailing whitespace
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces/newlines with a single space
    return text

# Extract all code snippets written in Markdown triple backtick format
def extract_code_snippets(text: str) -> list[str]:
    # Matches code blocks like ```...``` across multiple lines
    return re.findall(r"```[\s\S]*?```", text)

# Extract all URLs from the input text
def extract_links(text: str) -> list[str]:
    # Match HTTP/HTTPS URLs that are non-whitespace
    return re.findall(r"https?://\S+", text)

# Check if the prompt is valid: minimum length and at least one alphanumeric character
def is_valid_prompt(text: str) -> bool:
    return len(text.strip()) > 3 and any(c.isalnum() for c in text)
