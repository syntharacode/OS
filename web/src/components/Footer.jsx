// Footer component for the Synthara OS web UI
// Displays static footer text with dynamic current year

export default function Footer() {
  return (
    <footer className="w-full border-t p-4 text-center text-sm text-gray-500">
      {/* Dynamic year rendering and static project tagline */}
      Synthara OS © {new Date().getFullYear()} • Built for crypto & tech
    </footer>
  );
}
