// src/App.jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/Layout";

// Páginas
import Home from "./pages/Home";
import Login from "./pages/Login";
import Cadastro from "./pages/Cadastro";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* TODAS AS ROTAS COM O MESMO LAYOUT */}
        <Route element={<Layout />}>

          {/* PÁGINAS */}
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/cadastro" element={<Cadastro />} />

        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;
