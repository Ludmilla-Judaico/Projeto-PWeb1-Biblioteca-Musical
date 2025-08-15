from flask import render_template, url_for 
from app import app

import servicos

@app.route('/')
def homepage():
    return render_template('musicotecahome.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/album')
def album():
    # album = carregar_album()
    return render_template('descricao_album.html', album=album)