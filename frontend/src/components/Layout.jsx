// // src/components/Layout.jsx
// import { Outlet } from "react-router-dom";
// import NavbarHome from "./NavbarHome";
// import Footer from "./Footer";

// export default function Layout() {
//   return (
//     <>
//       <NavbarHome />
//       <Outlet /> 
//       <Footer />
//     </>
//   );
// }

import { Outlet, useLocation } from "react-router-dom";
import Navbar from "./NavbarHome";
import Footer from "./Footer";

function Layout() {
  const { pathname } = useLocation();

  // PÁGINAS SEM NAV
  const hideNav = pathname === "/login" || pathname === "/cadastro";

  return (
    <>
      {!hideNav && <Navbar />}
      <Outlet />
      {!hideNav && <Footer />}
    </>
  );
}

export default Layout;
