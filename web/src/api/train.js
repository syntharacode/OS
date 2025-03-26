import axios from "axios";

export async function trainLLM(texts = []) {
  if (!Array.isArray(texts) || texts.length === 0) {
    throw new Error("Training data must be a non-empty array of strings.");
  }

  try {
    const response = await axios.post("/api/llm/train", { texts });
    return response.data;
  } catch (error) {
    console.error("[SyntharaOS] Training failed:", error);
    throw error;
  }
}