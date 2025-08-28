from flask import render_template, url_for, redirect, session, request, flash, abort
from . import app
from .funcoes.albuns import *
from .funcoes.fav import *
from .funcoes.user import *
from .funcoes.biblioteca import *


#==========================ROTAS PÁGINAS================================

@app.route('/admin')
def admin():
    return render_template('admin.html')

EMAIL_ADMIN = "admin@email.com"
SENHA_ADMIN = "12345"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        email = request.form['email_login']
        senha = request.form['senha_login']

        if email == EMAIL_ADMIN and senha == SENHA_ADMIN:
            flash('Admin logado!')
            return redirect('/admin')

        if authenticator(email, senha):
            nome, foto = dados_associados(email)
            session['usuario'] = nome
            session['email'] = email
            session['foto'] = foto

            return redirect('/')

        flash('Email ou senha inválidos, tente novamente', 'error')
        return redirect('/login')     
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user = request.form['nome-user']
        email_user = request.form['email-user']
        senha_user = request.form['senha-user']
        signin(user, email_user, senha_user)
        flash("Cadastro realizado com sucesso :)", "sucess")
        return redirect('/')
    
    return render_template('signin.html')

@app.route('/')
def homepage():
    if 'usuario' not in session:
        return redirect('/login')
    usuario = session['usuario']
    albuns = carregar_album()
    return render_template('musicotecahome.html', albuns=albuns, usuario=usuario)

@app.route('/profile')
def profile():
    if 'usuario' not in session:
        return redirect('/login')
    usuario = session['usuario']
    foto = session['foto']
    favoritos = carregar_favoritos(usuario)

    return render_template('profile.html', favoritos=favoritos, usuario=usuario, foto=foto)

@app.route('/profile/biblioteca')
def minha_biblioteca():
    if 'usuario' not in session:
        return redirect('/login')
    usuario = session['usuario']
    foto = session['foto']
    biblioteca = carregar_biblioteca(usuario)

    return render_template('biblioteca.html', usuario=usuario, foto=foto, biblioteca=biblioteca, check_in_biblioteca=check_in_biblioteca)

@app.route('/profile/favoritos')
def favoritos():
    if 'usuario' not in session:
        return redirect('/login')
    usuario = session['usuario']
    foto = session['foto']
    favoritos = carregar_favoritos(usuario)
    return render_template('favoritos.html', usuario=usuario, foto=foto, favoritos=favoritos, check_in_fav=check_in_fav)

@app.route('/profile/edit', methods=['GET', 'POST'])
def edit_profile():
    if 'usuario' not in session:
        return redirect('/login')
    print("Sessão atual:", dict(session))
    
    usuario = session.get('usuario')
    email = session.get('email')
    foto = session.get('foto')
    if request.method == 'POST':
        novo_usuario = request.form['novo_usuario']
        novo_email = request.form['novo_email']
        nova_senha = request.form['nova_senha']
        nova_foto = request.form['nova_foto']

        edit_user(novo_usuario, novo_email, nova_senha, nova_foto)

        session['usuario'] = novo_usuario
        session['email'] = novo_email
        session['foto'] = nova_foto

        flash('Informações atualizadas com sucesso!')
        return redirect(url_for('app.profile'))
    return render_template('edit.html', usuario=usuario, email=email, foto=foto)
    

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/login')


@app.route('/album/<album_id>')
def album(album_id):
    album = comparar_id(album_id)

    musicas = carregar_discografia(album_id)

    usuario = session['usuario']
    inicializar_biblioteca()

    return render_template('descricao_album.html', usuario=usuario, album=album, musicas=musicas,
                            album_id=album_id, check_in_fav=check_in_fav, check_in_biblioteca=check_in_biblioteca)

@app.route('/favoritar/<album_id>')
def favoritar(album_id):
    if 'usuario' not in session:
        return redirect(url_for('app.login'))
    inicializar_favoritos()
    
    capa = next(a['capa'] for a in carregar_album() if a['album_id'] == album_id)
    usuario = session['usuario']

    if check_in_fav(album_id, usuario):
        remover_favorito(album_id)
        flash('Álbum removido dos favoritos')
        return redirect('/album/<album_id>')
    else:
        salvar_favorito(usuario, album_id, capa)
        flash('Álbum favoritado com sucesso!')
        return redirect('/profile/favoritos')

@app.route('/add_biblioteca/<album_id>')
def add_biblioteca(album_id):
    if 'usuario' not in session:
        return redirect(url_for('app.login'))
    inicializar_biblioteca()
    
    capa = next(a['capa'] for a in carregar_album() if a['album_id'] == album_id)
    usuario = session['usuario']

    if check_in_biblioteca(album_id, usuario):
        remover_da_biblioteca(album_id)
        flash('Álbum removido da biblioteca')
        return redirect('/profile/biblioteca')
    else:
        salvar_na_biblioteca(usuario, album_id, capa)
        flash('Álbum salvo na biblioteca')
        return redirect('/profile/biblioteca')


@app.route('/destino', methods=["POST"])
def salvar ():
    capa = request.form['capa']
    nome = request.form['nome']
    lancamento = request.form['lancamento']
    genero = request.form['genero']
    artista = request.form['artista']
    foto_bio = request.form['foto_bio']
    biografia = request.form['biografia']
    spotify = request.form['spotify']
    musicas = request.form['musicas']
    salvar_album(capa,nome,lancamento,genero,artista,foto_bio,biografia,spotify)
    salvar_musicas(musicas)

    flash('Álbum cadastrado com sucesso!')
    return redirect('/admin')

@app.route("/review", methods=["POST"])
def review():
    if request.method == "POST":
        album_id = request.form["album_id"]
        review = request.form["review"]
        salvar_comentario(album_id,review)

        return redirect('/')

#==========================ROTAS ERROS================================

@app.errorhandler(404)
def page_not_found(err):
    print("Handler 404 chamado!")
    return render_template("erros/404.html"), err.code
