from flask import render_template, url_for, redirect, session
from . import app

@app.route('/')
def homepage():
    return render_template('musicotecahome.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/album')
def album():
    return render_template('descricao_album.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')