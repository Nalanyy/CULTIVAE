from models import db

class Planta(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    imagem = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
