import argparse
from backend.models.trainer import fine_tune_model


def main():
    parser = argparse.ArgumentParser(description="Train SyntharaOS with custom prompts")
    parser.add_argument("--file", type=str, required=True, help="Path to text file with training prompts")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        texts = [line.strip() for line in f.readlines() if line.strip()]

    if not texts:
        print("[!] No valid training texts found.")
        return

    print(f"[+] Fine-tuning on {len(texts)} prompts...")
    fine_tune_model(texts)
    print("[✓] Training complete.")


if __name__ == "__main__":
    main()