from flask import Blueprint, render_template
from models.artigo import Artigo

artigos_bp = Blueprint("artigos", __name__)

@artigos_bp.route("/artigos")
def artigos():
    artigos = Artigo.query.all()
    return render_template("artigos.html", artigos=artigos)
