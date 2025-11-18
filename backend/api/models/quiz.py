from models import db

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pergunta = db.Column(db.Text, nullable=False)
    resposta_correta = db.Column(db.String(200), nullable=False)
