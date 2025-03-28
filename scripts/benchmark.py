# Import time module to measure inference durations
import time

# Import Synthara's model inference function
from backend.models.infer import generate_response

# Benchmark the model's average response time over multiple runs
def benchmark_model(prompt: str = "Define Solana in 1 sentence.", runs: int = 5):
    durations = []

    # Run the inference multiple times and collect durations
    for _ in range(runs):
        start = time.time()                    # Start timestamp
        _ = generate_response(prompt)          # Call LLM
        end = time.time()                      # End timestamp
        durations.append(end - start)          # Store elapsed time

    # Compute average latency
    avg = sum(durations) / len(durations)

    # Print benchmark results
    print("\n--- Benchmark Results ---")
    print(f"Prompt: {prompt}")
    print(f"Runs: {runs}")
    print(f"Average Latency: {avg:.2f}s")
    print(f"All Latencies: {', '.join(f'{d:.2f}s' for d in durations)}")

# Execute the benchmark when run as a script
if __name__ == "__main__":
    benchmark_model()
