from flask import Blueprint, render_template

favoritos_bp = Blueprint("favoritos", __name__)

@favoritos_bp.route("/favoritos")
def favoritos():
    return render_template("favoritos.html")
