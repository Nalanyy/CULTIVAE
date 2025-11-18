from flask import Blueprint, render_template

dicas_bp = Blueprint("dicas", __name__)

@dicas_bp.route("/dicas")
def dicas():
    return render_template("dicas.html")
