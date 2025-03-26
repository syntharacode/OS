import { useState } from "react";
import axios from "axios";

export default function TextInput() {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleQuery = async () => {
    if (!input.trim()) return;
    setLoading(true);
    try {
      const res = await axios.post("/api/llm/query", {
        input,
        max_tokens: 100,
        temperature: 0.7,
      });
      setOutput(res.data.response);
    } catch (err) {
      console.error("LLM query failed:", err);
      setOutput("Error: Unable to reach Synthara OS");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <textarea
        className="w-full h-40 p-2 border rounded"
        placeholder="Type your training or query prompt here..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        className="mt-2 px-4 py-2 bg-blue-600 text-white rounded"
        onClick={handleQuery}
        disabled={loading}
      >
        {loading ? "Processing..." : "Send to Synthara OS"}
      </button>
      {output && (
        <div className="mt-4 p-3 border rounded bg-gray-100">
          <strong>Output:</strong>
          <pre className="whitespace-pre-wrap">{output}</pre>
        </div>
      )}
    </div>
  );
}