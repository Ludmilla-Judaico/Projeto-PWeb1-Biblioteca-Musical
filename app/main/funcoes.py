from flask import session
import csv, os
#==================FUNÇÕES====================
caminho_albuns_lud = 'data/albuns-lud.csv'

def carregar_albuns():
    if not os.path.exists(caminho_albuns_lud):
        with open(caminho_albuns_lud, 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['id', 'nome', 'artista', 'capa'])
            albuns = [
                ["1","album","Lana Del Rey","https://upload.wikimedia.org/wikipedia/pt/thumb/4/47/LanaDelRey_BornToDie.jpg/250px-LanaDelRey_BornToDie.jpg"]
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
            writer.writerow(["usuario", "album_id", "capa"])

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

def salvar_favorito(usuario, album_id, capa):
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
            
def edit_user(novo_usuario, novo_email, nova_senha, nova_foto):
    with open("data/usuarios.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for i in range(len(leitor)):
            if session['usario'] == leitor[i][0]:
                leitor[i][0] = novo_usuario
                leitor[i][1] = novo_email
                leitor[i][2] = nova_senha
                leitor[i][3] = nova_foto
                break
            