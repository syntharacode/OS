import AppRoutes from "./routes";
import Header from "./components/Header";
import "./styles/globals.css";

export default function App() {
  return (
    <div className="min-h-screen bg-white text-black">
      <Header />
      <main>
        <AppRoutes />
      </main>
    </div>
  );
}
