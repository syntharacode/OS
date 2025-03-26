import time
from backend.models.infer import generate_response


def benchmark_model(prompt: str = "Define Solana in 1 sentence.", runs: int = 5):
    durations = []
    for _ in range(runs):
        start = time.time()
        _ = generate_response(prompt)
        end = time.time()
        durations.append(end - start)

    avg = sum(durations) / len(durations)
    print("\n--- Benchmark Results ---")
    print(f"Prompt: {prompt}")
    print(f"Runs: {runs}")
    print(f"Average Latency: {avg:.2f}s")
    print(f"All Latencies: {', '.join(f'{d:.2f}s' for d in durations)}")


if __name__ == "__main__":
    benchmark_model()