# Import the fine-tuning function from the model trainer module
from backend.models.trainer import fine_tune_model

# Import utility to fetch recently logged prompts from memory service
from backend.services.memory_service import get_recent_prompts

# Entry point for standalone script execution
if __name__ == "__main__":
    print("[SyntharaOS] Collecting recent prompts for training...")

    # Fetch the latest 20 prompts stored in the system
    prompts = get_recent_prompts(limit=20)

    # Extract raw prompt text from database records
    texts = [p.prompt for p in prompts]

    # If prompts are available, initiate training
    if texts:
        print(f"[✓] Training on {len(texts)} prompts")
        fine_tune_model(texts)
        print("[✓] Training complete.")
    else:
        print("[!] No prompts found for training.")
