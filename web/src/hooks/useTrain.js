import { useState } from "react";
import { trainLLM } from "@/api/llm";

export function useTrain() {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  const train = async (texts) => {
    setLoading(true);
    try {
      const res = await trainLLM(texts);
      setStatus(res.message);
    } catch (err) {
      setStatus("Training failed");
    } finally {
      setLoading(false);
    }
  };

  return { train, status, loading };
}