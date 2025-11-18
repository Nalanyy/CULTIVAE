from models import db

class Artigo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.Text)
