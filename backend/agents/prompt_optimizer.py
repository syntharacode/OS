from transformers import pipeline

# Simple zero-shot prompt scorer using HuggingFace pipeline
# Future extension: replace with real scoring model (e.g., reward model)

class PromptOptimizer:
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def score_prompt(self, prompt: str, labels: list[str] = None) -> dict:
        if labels is None:
            labels = ["relevant", "irrelevant", "technical", "off-topic"]

        result = self.classifier(prompt, candidate_labels=labels)
        scored = {label: score for label, score in zip(result['labels'], result['scores'])}
        return dict(sorted(scored.items(), key=lambda x: x[1], reverse=True))


optimizer = PromptOptimizer()