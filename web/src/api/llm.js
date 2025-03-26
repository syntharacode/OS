import axios from "axios";

export async function queryLLM(input, options = {}) {
  const payload = {
    input,
    max_tokens: options.max_tokens || 100,
    temperature: options.temperature || 0.7,
  };
  const res = await axios.post("/api/llm/query", payload);
  return res.data;
}

export async function trainLLM(texts) {
  const res = await axios.post("/api/llm/train", { texts });
  return res.data;
}