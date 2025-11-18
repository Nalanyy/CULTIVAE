from flask import Blueprint, render_template, request, redirect, url_for, session
from models.cultivario import Planta
from models import db
import os
from config import Config

from flask import Blueprint, render_template, session, request, jsonify
from models import db, Favorite


cultivario_bp = Blueprint("cultivario", __name__)
plantas = [
    {"nome": "Tomate", "descricao": "Rústico, fácil de cuidar, ideal para vasos.", "img": "tomate.jpg"},
    {"nome": "Girassol", "descricao": "Adora o sol, ideal para jardins ensolarados.", "img": "girassol.jpg"},
    {"nome": "Manjericão", "descricao": "Aroma suave, ideal para espaços pequenos.", "img": "manjericao.jpg"},
    {"nome": "Hortelã", "descricao": "Refrescante e fácil de cuidar.", "img": "hortela.jpg"},
    {"nome": "Lavanda", "descricao": "Aroma relaxante e flores lindas.", "img": "lavanda.jpg"}
]
@cultivario_bp.route("/cultivario")
def cultivario():
    # plantas = Planta.query.all()
    return render_template("cultivario.html", plantas = plantas, active_page='cultivario')


@cultivario_bp.route('/meu_cultivario')
def meu_cultivario():
    user_id = session.get('user_id')
    favorites = []
    if user_id:
        favorites = [fav.plant_name for fav in Favorite.query.filter_by(user_id=user_id).all()]
    return render_template('meu_cultivario.html', favorites=favorites, active_page='meu_cultivario')

@cultivario_bp.route('/add_favorite', methods=['POST'])
def add_favorite():
    if 'user_id' not in session:
        return jsonify({'error': 'Não autenticado'}), 401
    data = request.get_json()
    plant = data.get('plant')
    fav = Favorite.query.filter_by(user_id=session['user_id'], plant_name=plant).first()
    if not fav:
        db.session.add(Favorite(user_id=session['user_id'], plant_name=plant))
        db.session.commit()
    return jsonify({'message': 'Adicionado aos favoritos!'})

@cultivario_bp.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    if 'user_id' not in session:
        return jsonify({'error': 'Não autenticado'}), 401
    data = request.get_json()
    plant = data.get('plant')
    fav = Favorite.query.filter_by(user_id=session['user_id'], plant_name=plant).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
    return jsonify({'message': 'Removido dos favoritos!'})
