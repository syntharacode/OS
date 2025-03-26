import { useState } from "react";
import { queryLLM } from "@/api/llm";

export function useLLM() {
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const ask = async (input, options = {}) => {
    setLoading(true);
    const res = await queryLLM(input, options);
    setOutput(res.response);
    setLoading(false);
  };

  return { output, ask, loading };
}