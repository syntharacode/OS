import numpy as np
import evaluate

# Load standard NLP metrics from HuggingFace Evaluate
bleu = evaluate.load("bleu")
rouge = evaluate.load("rouge")
f1_metric = evaluate.load("f1")


def compute_bleu(preds: list[str], refs: list[str]) -> float:
    return bleu.compute(predictions=preds, references=[[r] for r in refs])['bleu']


def compute_rouge(preds: list[str], refs: list[str]) -> dict:
    return rouge.compute(predictions=preds, references=refs)


def compute_f1(preds: list[str], refs: list[str]) -> float:
    return f1_metric.compute(predictions=preds, references=refs)['f1']


def evaluate_model(preds: list[str], refs: list[str]) -> dict:
    return {
        "bleu": round(compute_bleu(preds, refs), 4),
        "f1": round(compute_f1(preds, refs), 4),
        **compute_rouge(preds, refs),
    }