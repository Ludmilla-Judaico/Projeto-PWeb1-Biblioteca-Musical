from flask import render_template, url_for, redirect, session, request, flash
import csv, os
from . import app

#==================FUNÇÕES====================
caminho_albuns_lud = 'data/albuns-lud.csv'

def carregar_albuns():
    if not os.path.exists(caminho_albuns_lud):
        with open(caminho_albuns_lud, 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['id', 'nome', 'artista', 'capa'])
            albuns = [
                ["1","album","Lana Del Rey","https://upload.wikimedia.org/wikipedia/en/5/55/Michael_Jackson_-_Thriller.png"]
            ]
            for album in albuns:
                writer.writerow(album)
        
    albuns = []
    with open(caminho_albuns_lud, newline='', encoding='utf-8') as arquivo:
        reader = csv.DictReader(arquivo)
        for row in reader:
            row["id"] = str(row["id"])
            albuns.append(row) 
    return albuns

caminho_favoritos = 'data/favoritos.csv'

def inicializar_favoritos():
    if not os.path.exists(caminho_favoritos):
        os.makedirs(os.path.dirname(caminho_favoritos), exist_ok=True)
        with open(caminho_favoritos, "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["usuario", "album_id"])

def carregar_favoritos(usuario):
    favoritos = []
    if not os.path.exists(caminho_favoritos):
        return favoritos
    
    with open(caminho_favoritos, newline='', encoding='utf-8') as arquivo:
        reader = csv.DictReader(arquivo)
        for row in reader:
            if row['usuario'] == usuario:
                favoritos.append(str(row['album_id']))
    return favoritos

def salvar_favorito(usuario, album_id):
    inicializar_favoritos()

    favoritos = []
    with open(caminho_favoritos, newline="", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        for row in reader:
            if row["usuario"] == usuario:
                favoritos.append(row["album_id"])
    
    if album_id not in favoritos:
        with open(caminho_favoritos, "a", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([usuario, album_id])

def signin(user, email, senha):
    with open('data/usuarios.csv', 'a', newline="", encoding="utf-8") as arquivo_user:
        writer = csv.writer(arquivo_user)
        writer.writerow([user, email, senha])


#==========================ROTAS================================
@app.route('/')
def homepage():
    albuns = carregar_albuns()
    return render_template('musicotecahome.html', albuns=albuns)

@app.route('/login', methods=['GET', 'POST'])
def login():
    session['usuario'] = 'ludmilla'
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user = request.form['nome-user']
        email_user = request.form['email-user']
        senha_user = request.form['senha-user']
        signin(user, email_user, senha_user)
        flash("Cadastro realizado com sucesso :)", "success")
        return redirect(url_for('app.cadastro'))
    
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

@app.routes('/destino', methods=["POST"])
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