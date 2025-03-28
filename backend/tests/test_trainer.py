# Import the fine-tuning function from the trainer module
from backend.models.trainer import fine_tune_model

# Unit test for validating the fine-tuning pipeline with a small prompt set
def test_fine_tune_small_prompt():
    # Define a minimal list of training prompts
    sample_prompts = [
        "Explain what a smart contract is in one sentence.",
        "Define the purpose of a crypto wallet.",
    ]

    try:
        # Attempt to fine-tune the model with the provided prompts
        model = fine_tune_model(sample_prompts)

        # Assert that a model object is returned
        assert model is not None

    except Exception as e:
        # Fail the test if any exception occurs
        assert False, f"Fine-tuning failed: {e}"
