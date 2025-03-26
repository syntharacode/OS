import { useState, useEffect } from "react";

export default function LogViewer() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("/api/system/logs")
        .then((res) => res.json())
        .then((data) => {
          if (data && Array.isArray(data.logs)) setLogs(data.logs);
        })
        .catch(() => {});
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="mt-6 bg-black text-green-400 p-4 rounded text-sm h-60 overflow-y-scroll">
      <h2 className="font-bold text-white mb-2">Synthara Logs</h2>
      <pre className="whitespace-pre-wrap">
        {logs.length > 0 ? logs.join("\n") : "Waiting for logs..."}
      </pre>
    </div>
  );
}