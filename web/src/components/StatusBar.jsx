import { useState, useEffect } from "react";

export default function StatusBar() {
  const [status, setStatus] = useState("Connecting...");

  useEffect(() => {
    const check = async () => {
      try {
        const res = await fetch("/api");
        const json = await res.json();
        if (json.message) setStatus("Online");
      } catch {
        setStatus("Offline");
      }
    };
    check();
    const interval = setInterval(check, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="fixed bottom-4 right-4 px-3 py-1 rounded bg-black text-white text-xs shadow">
      Synthara OS: {status}
    </div>
  );
}