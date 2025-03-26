from backend.models.trainer import fine_tune_model
from backend.db.connection import get_db
from sqlalchemy.orm import Session

# Simple feedback loop agent that collects user feedback texts
# and uses them for fine-tuning after aggregation
class FeedbackLoopAgent:
    def __init__(self):
        self.feedback_buffer = []
        self.threshold = 5  # How many feedbacks to accumulate before fine-tuning

    def add_feedback(self, text: str):
        self.feedback_buffer.append(text)
        if len(self.feedback_buffer) >= self.threshold:
            self._trigger_training()

    def _trigger_training(self):
        print("[SyntharaOS] Feedback threshold reached. Fine-tuning...")
        fine_tune_model(self.feedback_buffer)
        self.feedback_buffer.clear()


feedback_agent = FeedbackLoopAgent()