import os

class Config:
    SECRET_KEY = "Cultvae-Jhonatas_Nalany"
    SQLALCHEMY_DATABASE_URI = "sqlite:///cultivae.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "static/imagens")
