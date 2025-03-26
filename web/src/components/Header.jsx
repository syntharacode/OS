import { Link, useLocation } from "react-router-dom";

export default function Header() {
  const { pathname } = useLocation();

  const navLink = (to, label) => (
    <Link
      to={to}
      className={`px-3 py-2 rounded-md text-sm font-medium ${
        pathname === to ? "bg-blue-600 text-white" : "text-gray-700 hover:bg-gray-200"
      }`}
    >
      {label}
    </Link>
  );

  return (
    <header className="w-full border-b bg-white sticky top-0 z-10 shadow-sm">
      <div className="max-w-6xl mx-auto flex items-center justify-between px-6 py-3">
        <h1 className="text-xl font-bold text-blue-700">Synthara OS</h1>
        <nav className="flex gap-4">
          {navLink("/", "Home")}
          {navLink("/train", "Train")}
          {navLink("/about", "About")}
        </nav>
      </div>
    </header>
  );
}