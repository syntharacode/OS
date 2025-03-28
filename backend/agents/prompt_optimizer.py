# Import the HuggingFace pipeline tool for prebuilt NLP tasks
from transformers import pipeline

# PromptOptimizer is a lightweight scoring agent that evaluates prompts
# using a zero-shot classification pipeline to label them semantically.
# 
# Future plan: swap this for a fine-tuned reward model or policy model
class PromptOptimizer:
    def __init__(self):
        # Load a zero-shot classifier model (BART large) from HuggingFace
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )

    # Score a given prompt against a list of semantic labels
    def score_prompt(self, prompt: str, labels: list[str] = None) -> dict:
        # If no labels provided, use a default set
        if labels is None:
            labels = ["relevant", "irrelevant", "technical", "off-topic"]

        # Run the zero-shot classifier
        result = self.classifier(prompt, candidate_labels=labels)

        # Extract labels and their scores, return as sorted dictionary
        scored = {label: score for label, score in zip(result['labels'], result['scores'])}
        return dict(sorted(scored.items(), key=lambda x: x[1], reverse=True))


# Global optimizer instance for scoring prompts across the system
optimizer = PromptOptimizer()
