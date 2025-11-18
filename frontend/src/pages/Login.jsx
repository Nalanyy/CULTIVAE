import { Link } from "react-router-dom";
import "./Login.css";

function Login() {
  return (
    <div className="login-page">

      <div className="login-left"></div>

      <div className="login-right">

        <div className="login-header">
          <Link to="/" className="voltar-home">← Voltar</Link>
          <h1>LOGIN</h1>
          <p>Entre na sua conta ou cadastre-se!</p>
        </div>

        <div className="login-form-area">

          <form className="login-form" method="POST">

            <div className="form-group">
              <label>Usuário:</label>
              <input type="text" placeholder="Digite seu usuário" required />
            </div>

            <div className="form-group">
              <label>Senha:</label>
              <input type="password" placeholder="Digite sua senha" required />
            </div>

            <button type="submit">Entrar</button>

            <p>Não tem uma conta? <Link to="/cadastro">Cadastre-se</Link></p>

          </form>

        </div>

      </div>

    </div>
  );
}

export default Login;
