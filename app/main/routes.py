from flask import render_template, url_for, redirect, session, request, flash
import csv, os
from . import app
from .funcoes import carregar_albuns, carregar_favoritos, salvar_favorito, nome_associado, authenticator
from .servicos import salvar_album, salvar_musicas

def signin(user, email, senha):
    if not os.path.exists('data/usuarios.csv'):
        with open('data/usuarios.csv', 'w', newline="", encoding="utf-8") as arquivo_user:
            writer = csv.writer(arquivo_user)
            writer.writerow(['usuário', 'email', 'senha'])

    with open('data/usuarios.csv', 'a', newline="", encoding="utf-8") as arquivo_user:
        writer = csv.writer(arquivo_user)
        writer.writerow([user, email, senha])


#==========================ROTAS PÁGINAS================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        user_email = request.form['email_login']
        senha = request.form['senha_login']
        print("pegou infos")
        if authenticator(user_email, senha):
            nome_user = nome_associado(user_email)
            session['usuario'] = nome_user

            print('entrou')
            print(session['usuario'], nome_user)
            return redirect('/')

        print('não entrou')
        return redirect('/login')     
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user = request.form['nome-user']
        email_user = request.form['email-user']
        senha_user = request.form['senha-user']
        signin(user, email_user, senha_user)
        flash("Cadastro realizado com sucesso :)", "success")
        return redirect('/')
    
    return render_template('signin.html')

@app.route('/')
def homepage():
    if 'usuario' not in session:
        return redirect('/login')
    usuario = session['usuario']
    albuns = carregar_albuns()
    return render_template('musicotecahome.html', albuns=albuns, usuario=usuario)

@app.route('/profile')
def profile():
    if 'usuario' not in session:
        return redirect('/login')
    usuario = session['usuario']
    albuns = carregar_albuns()
    favoritos_ids = carregar_favoritos(usuario)
    favoritos = [a for a in albuns if a['id'] in favoritos_ids]

    print("Usuário logado:", usuario)
    print("Todos os álbuns:", [a["id"] for a in albuns])
    print("IDs de favoritos do usuário:", favoritos_ids)
    print("Albuns filtrados como favoritos:", [a["id"] for a in favoritos])

    return render_template('profile.html', favoritos=favoritos, usuario=usuario)

@app.route('/profile/biblioteca')
def minha_biblioteca():
    return render_template('biblioteca.html')

@app.route('/profile/favoritos')
def favoritos():
    return render_template('favoritos.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Deslogado com sucesso, volte sempre!')
    return redirect('/login')

@app.route('/album')
def album():
    return render_template('descricao_album.html')

#======================ROTAS FUNÇÕES=====================

@app.route('/favoritar/<album_id>')
def favoritar(album_id):
    if 'usuario' not in session:
        flash('É necessário estar logado para favoritar um albúm!')
        return redirect(url_for('login'))
    
    usuario = session['usuario']

    salvar_favorito(usuario, album_id)
    return redirect('/profile')

@app.route('/destino', methods=["POST"])
def salvar ():
    id = request.form['id']
    capa = request.form['capa']
    nome = request.form['nome']
    lancamento = request.form['lancamento']
    genero = request.form['genero']
    artista = request.form['artista']
    foto_bio = request.form['genefoto_bioro']
    biografia = request.form['biografia']
    spotify = request.form['spotify']
    musicas = request.form['musicas']
    armazenar = salvar_album(id,capa,nome,lancamento,genero,artista,foto_bio,biografia,spotify)