import { Link } from "react-router-dom";
import "./Cadastro.css"; // vamos mover o CSS para um arquivo separado

function Cadastro() {
  return (
    <div className="cadastro-page">

      {/* LADO ESQUERDO */}
      <div className="cadastro-left"></div>

      {/* LADO DIREITO */}
      <div className="cadastro-right">

        {/* CABEÇALHO VERDE */}
        <div className="cadastro-header">
          <Link to="/" className="voltar-home">← Voltar</Link>
          <h1>CADASTRO</h1>
          <p>Crie sua conta para começar a cultivar!</p>
        </div>

        {/* FORM */}
        <div className="cadastro-form-area">
          <form className="cadastro-form" method="POST">

            <div className="form-group">
              <label>Nome:</label>
              <input type="text" placeholder="Digite seu nome completo" required />
            </div>

            <div className="form-group">
              <label>E-mail:</label>
              <input type="email" placeholder="Digite seu e-mail" required />
            </div>

            <div className="form-group">
              <label>Senha:</label>
              <input type="password" placeholder="Digite sua senha" required />
            </div>

            <div className="form-group">
              <label>Confirmar Senha:</label>
              <input type="password" placeholder="Confirme sua senha" required />
            </div>

            <button type="submit">Cadastrar</button>

            <p>
              Já tem uma conta? <Link to="/login">Faça login</Link>
            </p>

          </form>
        </div>

      </div>

    </div>
  );
}

export default Cadastro;
