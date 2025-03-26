import { useEffect, useState } from "react";

export function useStatusPing() {
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

  return status;
}