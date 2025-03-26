import { useState } from "react";
import TextInput from "../components/TextInput";
import TrainingButton from "../components/TrainingButton";
import OutputBox from "../components/OutputBox";

export default function TrainPage() {
  const [inputText, setInputText] = useState("");
  const [output, setOutput] = useState("");

  const handleSend = async () => {
    const res = await fetch("/api/llm/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input: inputText }),
    });
    const data = await res.json();
    setOutput(data.response);
  };

  return (
    <div className="max-w-3xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Train Synthara OS</h1>

      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter your training or query prompt..."
        className="w-full h-40 p-3 border rounded mb-4"
      />

      <div className="flex gap-4">
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded"
          onClick={handleSend}
        >
          Run Query
        </button>
        <TrainingButton texts={[inputText]} />
      </div>

      <OutputBox output={output} />
    </div>
  );
}