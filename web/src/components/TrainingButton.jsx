import { useState } from "react";
import { trainLLM } from "../api/train";

export default function TrainingButton({ texts }) {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleTrain = async () => {
    if (!Array.isArray(texts) || texts.length === 0) {
      alert("Please provide at least one training text.");
      return;
    }

    setLoading(true);
    setStatus(null);

    try {
      const res = await trainLLM(texts);
      setStatus(res.message);
    } catch (err) {
      setStatus("Training failed. Check console.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mt-4">
      <button
        onClick={handleTrain}
        disabled={loading}
        className="px-4 py-2 bg-green-600 text-white rounded"
      >
        {loading ? "Training..." : "Train Synthara OS"}
      </button>
      {status && <p className="mt-2 text-sm text-gray-700">{status}</p>}
    </div>
  );
}