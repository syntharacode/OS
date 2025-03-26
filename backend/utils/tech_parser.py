import re

# Extract technical terms from prompt

def extract_technologies(text: str) -> list[str]:
    tech_terms = [
        "solana", "ethereum", "blockchain", "wallet", "token", "smart contract",
        "node.js", "react", "docker", "api", "llm", "prompt", "hash", "ledger",
        "web3", "metamask", "dapp", "defi", "rpc", "ganache", "graphql",
    ]

    found = [term for term in tech_terms if re.search(rf"\\b{term}\\b", text, re.IGNORECASE)]
    return found


def is_technical(text: str) -> bool:
    return len(extract_technologies(text)) > 0