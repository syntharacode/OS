from backend.models.trainer import fine_tune_model
from backend.services.memory_service import get_recent_prompts

if __name__ == "__main__":
    print("[SyntharaOS] Collecting recent prompts for training...")
    prompts = get_recent_prompts(limit=20)
    texts = [p.prompt for p in prompts]

    if texts:
        print(f"[✓] Training on {len(texts)} prompts")
        fine_tune_model(texts)
        print("[✓] Training complete.")
    else:
        print("[!] No prompts found for training.")