// src/pages/Home.jsx
import "./Home.css";

export default function Home() {
  return (
    <>
      <div className="home-container">
        <div className="home-inner">

          <img src="/img/folhas.jpg" alt="Folhas" className="banner" />

          <div className="home-content">
            <div className="home-left">
              <div className="texto-intro">
                <b>Cultivaê</b>: porque cuidar do mundo começa com uma semente.<br />
                O que parece pequeno hoje pode se tornar gigante amanhã, basta cultivar.<br /><br />
                Cadastre-se ou entre na sua conta!
              </div>
              <a href="/cadastro" className="btn-cadastro">Cadastre-se</a>
            </div>

            <div className="home-right">
              <div className="imagens-galeria">
                <img src="/img/flores.jpg" alt="Flores" />
                <img src="/img/arvore.jpg" alt="Árvore" />
                <img src="/img/mudas.jpg" alt="Muda" />
              </div>
            </div>
          </div>

        </div>
      </div>
    </>
  );
}
