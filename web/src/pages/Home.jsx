import { Link } from "react-router-dom";

export default function HomePage() {
  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">Welcome to Synthara OS</h1>
      <p className="text-gray-700 mb-6">
        This is a next-gen LLM Operating System focused on crypto, tech, and autonomous learning. Navigate to the train panel to get started.
      </p>
      <Link
        to="/train"
        className="inline-block bg-blue-600 text-white px-4 py-2 rounded shadow"
      >
        Start Training
      </Link>
    </div>
  );
}