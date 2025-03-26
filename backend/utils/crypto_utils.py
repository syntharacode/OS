import re

# Basic tools for identifying and tagging crypto-related entities in text

def detect_wallet_addresses(text: str) -> list[str]:
    # Very basic ETH/SOL wallet pattern
    return re.findall(r"\b(0x[a-fA-F0-9]{40}|[1-9A-HJ-NP-Za-km-z]{32,44})\b", text)


def extract_tokens(text: str) -> list[str]:
    keywords = ["usdc", "eth", "sol", "btc", "nft", "dao", "dex", "bridge"]
    return [kw for kw in keywords if re.search(rf"\\b{kw}\\b", text, re.IGNORECASE)]


def has_crypto_context(text: str) -> bool:
    return bool(detect_wallet_addresses(text)) or bool(extract_tokens(text))