from flask import Blueprint, render_template
from models.quiz import Quiz

quizzes_bp = Blueprint("quizzes", __name__)

@quizzes_bp.route("/quizzes")
def quizzes():
    # quizzes = Quiz.query.all()
    # return render_template("quizzes.html", quizzes=quizzes)
    return render_template("quizzes.html")
