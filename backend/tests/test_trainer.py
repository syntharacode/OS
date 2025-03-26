from backend.models.trainer import fine_tune_model


def test_fine_tune_small_prompt():
    sample_prompts = [
        "Explain what a smart contract is in one sentence.",
        "Define the purpose of a crypto wallet.",
    ]
    try:
        model = fine_tune_model(sample_prompts)
        assert model is not None
    except Exception as e:
        assert False, f"Fine-tuning failed: {e}"