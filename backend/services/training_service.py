# Import the fine-tuning function for the model
from backend.models.trainer import fine_tune_model

# Import the memory service to retrieve recent user prompts
from backend.services.memory_service import get_recent_prompts

# Central training control for Synthara OS
# Can be triggered manually or on schedule (e.g. via cron, event, or agent)

def run_recent_prompt_training():
    # Fetch a limited number of recent prompts from memory
    prompts = get_recent_prompts(limit=20)

    # Extract raw text content from prompt log entries
    texts = [p.prompt for p in prompts]

    # If prompts are available, trigger fine-tuning
    if texts:
        print(f"[SyntharaOS] Training on {len(texts)} recent prompts")
        fine_tune_model(texts)
        return True

    # No prompts available to train on
    return False
