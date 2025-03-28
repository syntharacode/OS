# Import the argument parser for command-line usage
import argparse

# Import the response generation function from SyntharaOS inference module
from backend.models.infer import generate_response

# Entry point for CLI-based model querying
def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Query SyntharaOS LLM")
    parser.add_argument("--prompt", type=str, required=True, help="Input prompt for the model")
    parser.add_argument("--max_tokens", type=int, default=100)
    parser.add_argument("--temperature", type=float, default=0.7)
    args = parser.parse_args()

    # Start the inference process
    print("[SyntharaOS] Generating response...")
    output = generate_response(
        prompt=args.prompt,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
    )

    # Print model output to terminal
    print("\n[Model Output]\n")
    print(output)

# Execute main() when the script is run directly
if __name__ == "__main__":
    main()
