export default function OutputBox({ output }) {
  if (!output) return null;

  return (
    <div className="mt-4 p-4 bg-gray-100 border rounded shadow-sm">
      <h2 className="font-semibold mb-2">Model Output</h2>
      <pre className="whitespace-pre-wrap break-words text-sm text-gray-800">
        {output}
      </pre>
    </div>
  );
}