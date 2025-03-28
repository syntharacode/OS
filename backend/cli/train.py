# Import command-line argument parser
import argparse

# Import the model fine-tuning function from SyntharaOS core model module
from backend.models.trainer import fine_tune_model

# Entry point for CLI-based fine-tuning
def main():
    # Set up argument parser for CLI usage
    parser = argparse.ArgumentParser(description="Train SyntharaOS with custom prompts")
    parser.add_argument("--file", type=str, required=True, help="Path to text file with training prompts")
    args = parser.parse_args()

    # Read training data from provided file
    with open(args.file, "r", encoding="utf-8") as f:
        texts = [line.strip() for line in f.readlines() if line.strip()]

    # Ensure we have valid training data
    if not texts:
        print("[!] No valid training texts found.")
        return

    # Start the fine-tuning process
    print(f"[+] Fine-tuning on {len(texts)} prompts...")
    fine_tune_model(texts)
    print("[✓] Training complete.")

# Execute main function if script is run directly
if __name__ == "__main__":
    main()
