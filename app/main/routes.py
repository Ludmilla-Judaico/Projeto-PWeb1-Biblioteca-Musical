from flask import render_template, url_for, redirect, session, request, flash
from . import app
from .funções import carregar_albuns, carregar_favoritos, salvar_favorito

#==========================ROTAS================================
@app.route('/')
def homepage():
    albuns = carregar_albuns()
    return render_template('musicotecahome.html', albuns=albuns)

@app.route('/login', methods=['GET', 'POST'])
def login():
    session['usuario'] = 'ludmilla'
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('signin.html')

@app.route('/biblioteca')
def minha_biblioteca():
    return render_template('biblioteca.html')

@app.route('/profile')
def profile():
    usuario = session['usuario']
    albuns = carregar_albuns()
    favoritos_ids = carregar_favoritos(usuario)
    favoritos = [a for a in albuns if a['id'] in favoritos_ids]

    print("Usuário logado:", usuario)
    print("Todos os álbuns:", [a["id"] for a in albuns])
    print("IDs de favoritos do usuário:", favoritos_ids)
    print("Albuns filtrados como favoritos:", [a["id"] for a in favoritos])

    return render_template('profile.html', favoritos=favoritos, usuario=usuario)

@app.route('/album')
def album():
    return render_template('descricao_album.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Deslogado com sucesso, volte sempre!')
    return redirect('/login')

#======================FAVORITAR=====================

@app.route('/favoritar/<album_id>')
def favoritar(album_id):
    if 'usuario' not in session:
        flash('É necessário estar logado para favoritar um albúm!')
        return redirect(url_for('login'))
    
    usuario = session['usuario']

    salvar_favorito(usuario, album_id)
    return redirect('/profile')