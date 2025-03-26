from backend.models.trainer import fine_tune_model
from backend.services.memory_service import get_recent_prompts

# Central training control for Synthara OS
# Can be triggered manually or on schedule

def run_recent_prompt_training():
    prompts = get_recent_prompts(limit=20)
    texts = [p.prompt for p in prompts]
    if texts:
        print(f"[SyntharaOS] Training on {len(texts)} recent prompts")
        fine_tune_model(texts)
        return True
    return False