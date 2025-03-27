# Import fine-tuning logic for the language model
from backend.models.trainer import fine_tune_model

# Database connector for accessing training data
from backend.db.connection import get_db

# Analytics service for retrieving prompt usage statistics
from backend.services.analytics_service import get_most_common_prompts


# AutoTrainer is responsible for monitoring prompt frequency and 
# automatically triggering model fine-tuning when certain thresholds are met
class AutoTrainer:
    def __init__(self):
        # Number of times a prompt must appear before it qualifies for training
        self.threshold = 10

    # Runs the analysis and invokes training if needed
    def analyze_and_train(self):
        print("[SyntharaOS] Running auto-training analysis...")

        # Get top 50 most used prompts with their usage counts
        prompts = get_most_common_prompts(limit=50)

        # Filter prompts that meet or exceed the threshold
        texts_to_train = [p['prompt'] for p in prompts if p['count'] >= self.threshold]

        # If qualifying prompts found, fine-tune the model with them
        if texts_to_train:
            print(f"[SyntharaOS] Auto-training with {len(texts_to_train)} prompts")
            fine_tune_model(texts_to_train)
        else:
            print("[SyntharaOS] No prompts passed threshold for training.")


# Initialize the auto-training engine
auto_trainer = AutoTrainer()
