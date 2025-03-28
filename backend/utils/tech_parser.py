# Import regex module for keyword matching
import re

# Extract technical terms from prompt

# Extract known technical keywords from the input text
def extract_technologies(text: str) -> list[str]:
    # Define a list of crypto/tech-related terms to look for
    tech_terms = [
        "solana", "ethereum", "blockchain", "wallet", "token", "smart contract",
        "node.js", "react", "docker", "api", "llm", "prompt", "hash", "ledger",
        "web3", "metamask", "dapp", "defi", "rpc", "ganache", "graphql",
    ]

    # Check for whole-word matches (case-insensitive) using regex
    found = [term for term in tech_terms if re.search(rf"\\b{term}\\b", text, re.IGNORECASE)]
    return found

# Determine if the input text is considered technical based on known keywords
def is_technical(text: str) -> bool:
    return len(extract_technologies(text)) > 0
