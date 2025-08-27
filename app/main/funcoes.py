from flask import session
import csv, os
#==================FUNÇÕES====================
caminho_albuns_lud = 'data/albuns-lud.csv'

# def carregar_albuns():
#     if not os.path.exists(caminho_albuns_lud):
#         with open(caminho_albuns_lud, 'w', newline='', encoding='utf-8') as arquivo:
#             writer = csv.writer(arquivo)
#             writer.writerow(['id', 'nome', 'artista', 'capa'])
#             albuns = [
#                 ["1","album","Lana Del Rey","https://upload.wikimedia.org/wikipedia/pt/thumb/4/47/LanaDelRey_BornToDie.jpg/250px-LanaDelRey_BornToDie.jpg"]
#             ]
#             for album in albuns:
#                 writer.writerow(album)
        
#     albuns = []
#     with open(caminho_albuns_lud, newline='', encoding='utf-8') as arquivo:
#         reader = csv.DictReader(arquivo)
#         for row in reader:
#             row["id"] = str(row["id"])
#             albuns.append(row) 
#     return albuns

caminho_favoritos = 'data/favoritos.csv'

def inicializar_favoritos():
    if not os.path.exists(caminho_favoritos):
        os.makedirs(os.path.dirname(caminho_favoritos), exist_ok=True)
        with open(caminho_favoritos, "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["usuario", "album_id", "capa"])

def carregar_favoritos(usuario):
    favoritos = []
    if not os.path.exists(caminho_favoritos):
        return favoritos
    with open(caminho_favoritos, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha['usuario'] == usuario:
                favoritos.append({
                    "album_id": linha["album_id"],
                    "capa": linha["capa"]
                })
    return favoritos

def salvar_favorito(usuario, album_id, capa):
    inicializar_favoritos()

    fav = []
    with open(caminho_favoritos, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["usuario"] == usuario:
                fav.append(linha["album_id"])
    
    if album_id not in fav:
        with open(caminho_favoritos, "a", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([usuario, album_id, capa])


def dados_associados(user_email):          
    with open("data/usuarios.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["email"] == user_email:
                nome = linha['usuário']
                foto = linha['foto']
                return nome, foto
            
def authenticator(user_email, senha):
    if os.path.exists('data/usuarios.csv'):
        with open('data/usuarios.csv', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if (linha['email'] == user_email) and (linha['senha'] == senha):
                    return True
            return False
    return False
            
def edit_user(novo_usuario=None, novo_email=None, nova_senha=None, nova_foto=None):
    with open("data/usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        linhas = []
        leitor = csv.DictReader(arquivo)
        dados = leitor.fieldnames
        for linha in leitor:
            if session['usuario'] == linha['usuário']:
                if novo_usuario:
                    linha['usuário'] = novo_usuario
                if novo_email:
                    linha['email'] = novo_email
                if nova_senha:
                    linha['senha'] = nova_senha
                if nova_foto:
                    linha['foto'] = nova_foto
            linhas.append(linha)

    with open("data/usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        
        escritor = csv.DictWriter(arquivo, fieldnames=dados)
        escritor.writeheader()
        escritor.writerows(linhas)

    if novo_usuario:
        session['usuario'] = novo_usuario
    if novo_email:
        session['email'] = novo_email
    if nova_foto:
        session['foto'] = nova_foto
            