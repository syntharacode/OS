# Import NumPy (optional here, but good for numerical extensions)
import numpy as np

# Import evaluation metric loaders from HuggingFace Evaluate
import evaluate

# Load standard NLP metrics from HuggingFace Evaluate
bleu = evaluate.load("bleu")         # BLEU score for translation-like tasks
rouge = evaluate.load("rouge")       # ROUGE score for summarization
f1_metric = evaluate.load("f1")      # F1 score for classification-style tasks

# Compute BLEU score between predicted and reference texts
def compute_bleu(preds: list[str], refs: list[str]) -> float:
    # Each reference must be a list of strings, even if only one reference per prediction
    return bleu.compute(predictions=preds, references=[[r] for r in refs])['bleu']

# Compute ROUGE scores between predictions and references
def compute_rouge(preds: list[str], refs: list[str]) -> dict:
    return rouge.compute(predictions=preds, references=refs)

# Compute F1 score between predictions and references
def compute_f1(preds: list[str], refs: list[str]) -> float:
    return f1_metric.compute(predictions=preds, references=refs)['f1']

# Aggregate all evaluation metrics into a single dictionary
def evaluate_model(preds: list[str], refs: list[str]) -> dict:
    return {
        "bleu": round(compute_bleu(preds, refs), 4),
        "f1": round(compute_f1(preds, refs), 4),
        **compute_rouge(preds, refs),  # ROUGE returns a dict with rouge1, rouge2, rougeL...
    }
