from flask import Flask
from flask_cors import CORS

from config import Config
from banco_dados.db_sqlite import bd
from modelos.user import User

# Blueprints
from blueprints.home.home_bp import home_bp
from blueprints.auth.auth_bp import auth_bp
from blueprints.cultivario.cultivario_bp import cultivario_bp
from blueprints.dicas.dicas_bp import dicas_bp
from blueprints.favoritos.favoritos_bp import favoritos_bp
from blueprints.artigos.artigos_bp import artigos_bp
from blueprints.quizzes.quizzes_bp import quizzes_bp


app = Flask(__name__)
CORS(app)

# Carregar configurações
app.config.from_object(Config)

# Inicializar banco
bd.init_app(app)

# Criar tabelas
with app.app_context():
    bd.create_all()

# Registrar blueprints
app.register_blueprint(home_bp, url_prefix="/home")
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(cultivario_bp, url_prefix="/cultivario")
app.register_blueprint(dicas_bp, url_prefix="/dicas")
app.register_blueprint(favoritos_bp, url_prefix="/favoritos")
app.register_blueprint(artigos_bp, url_prefix="/artigos")
app.register_blueprint(quizzes_bp, url_prefix="/quizzes")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
