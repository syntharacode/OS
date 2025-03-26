from backend.models.trainer import fine_tune_model
from backend.db.connection import get_db
from backend.services.analytics_service import get_most_common_prompts

# Automatically triggers model training based on prompt usage statistics
class AutoTrainer:
    def __init__(self):
        self.threshold = 10  # Number of prompt repetitions before triggering training

    def analyze_and_train(self):
        print("[SyntharaOS] Running auto-training analysis...")
        prompts = get_most_common_prompts(limit=50)
        texts_to_train = [p['prompt'] for p in prompts if p['count'] >= self.threshold]

        if texts_to_train:
            print(f"[SyntharaOS] Auto-training with {len(texts_to_train)} prompts")
            fine_tune_model(texts_to_train)
        else:
            print("[SyntharaOS] No prompts passed threshold for training.")


auto_trainer = AutoTrainer()