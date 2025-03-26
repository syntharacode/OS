import { useState } from "react";
import { queryLLM } from "@/api/llm";
import OutputBox from "@/components/OutputBox";

export default function QueryPage() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleQuery = async () => {
    if (!prompt.trim()) return;
    setLoading(true);
    const result = await queryLLM(prompt);
    setResponse(result.response);
    setLoading(false);
  };

  return (
    <div className="max-w-3xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Query Synthara OS</h1>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        className="w-full h-32 p-3 border rounded"
        placeholder="Type your question or command..."
      ></textarea>
      <button
        onClick={handleQuery}
        className="mt-2 px-4 py-2 bg-blue-600 text-white rounded"
        disabled={loading}
      >
        {loading ? "Loading..." : "Send"}
      </button>
      <OutputBox output={response} />
    </div>
  );
}