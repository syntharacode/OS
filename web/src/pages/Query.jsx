// Import React state management
import { useState } from "react";
// Import Synthara OS LLM query API function
import { queryLLM } from "@/api/llm";
// Import reusable output rendering component
import OutputBox from "@/components/OutputBox";

// Dedicated page for sending prompts to Synthara OS and receiving LLM output
export default function QueryPage() {
  // User input prompt
  const [prompt, setPrompt] = useState("");
  // Model-generated response
  const [response, setResponse] = useState("");
  // Track loading state for button/UX
  const [loading, setLoading] = useState(false);

  // Function to handle sending the prompt to the backend LLM API
  const handleQuery = async () => {
    if (!prompt.trim()) return; // Ignore empty prompts
    setLoading(true);           // Enter loading state
    const result = await queryLLM(prompt); // Call Synthara LLM
    setResponse(result.response);          // Store response for display
    setLoading(false);          // Exit loading state
  };

  return (
    <div className="max-w-3xl mx-auto p-6">
      {/* Page title */}
      <h1 className="text-2xl font-bold mb-4">Query Synthara OS</h1>

      {/* Input textarea for writing LLM prompt */}
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        className="w-full h-32 p-3 border rounded"
        placeholder="Type your question or command..."
      ></textarea>

      {/* Submit button to trigger the query */}
      <button
        onClick={handleQuery}
        className="mt-2 px-4 py-2 bg-blue-600 text-white rounded"
        disabled={loading}
      >
        {loading ? "Loading..." : "Send"}
      </button>

      {/* Component to display the model's response */}
      <OutputBox output={response} />
    </div>
  );
}
