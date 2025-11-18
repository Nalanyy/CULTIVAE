from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('cultivario.meu_cultivario'))
        else:
            flash('Usuário ou senha incorretos!', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']

        if senha != confirmar_senha:
            flash('As senhas não coincidem!', 'error')
            return redirect(url_for('auth.cadastro'))

        if User.query.filter((User.username == nome) | (User.email == email)).first():
            flash('Usuário ou e-mail já cadastrados!', 'error')
            return redirect(url_for('auth.cadastro'))

        user = User(username=nome, email=email)
        user.set_password(senha)
        db.session.add(user)
        db.session.commit()

        flash('Cadastro realizado com sucesso! Você já pode fazer login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('cadastro.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('auth.login'))
