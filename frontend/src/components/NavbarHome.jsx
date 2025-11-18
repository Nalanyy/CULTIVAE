// src/components/NavbarHome.jsx

import { Link } from "react-router-dom";
import "./NavbarHome.css";

export default function NavbarHome() {
  return (
    <nav className="navbar-home">
      <div className="logo">C U L T I V A Ê</div>
      <ul>
        <li><Link to="/" className="active">Home</Link></li>
        <li><Link to="/login">Login</Link></li>
      </ul>
    </nav>
  );
}
