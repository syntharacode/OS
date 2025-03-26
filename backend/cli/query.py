import argparse
from backend.models.infer import generate_response


def main():
    parser = argparse.ArgumentParser(description="Query SyntharaOS LLM")
    parser.add_argument("--prompt", type=str, required=True, help="Input prompt for the model")
    parser.add_argument("--max_tokens", type=int, default=100)
    parser.add_argument("--temperature", type=float, default=0.7)
    args = parser.parse_args()

    print("[SyntharaOS] Generating response...")
    output = generate_response(
        prompt=args.prompt,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
    )
    print("\n[Model Output]\n")
    print(output)


if __name__ == "__main__":
    main()