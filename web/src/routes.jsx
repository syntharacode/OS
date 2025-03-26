import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import TrainPage from "./pages/Train";
import AboutPage from "./pages/About";
import HomePage from "./pages/Home";

export default function AppRoutes() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/train" element={<TrainPage />} />
        <Route path="/about" element={<AboutPage />} />
      </Routes>
    </Router>
  );
}