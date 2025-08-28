import csv, os
caminho_favoritos = 'data/favoritos.csv'

#============================FUNÇÕES==============================

def inicializar_favoritos():
    if not os.path.exists(caminho_favoritos):
        os.makedirs(os.path.dirname(caminho_favoritos), exist_ok=True)
        with open(caminho_favoritos, "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["usuário", "album_id", "capa"])

#================================
def carregar_favoritos(usuario):
    favoritos = []
    if not os.path.exists(caminho_favoritos):
        return favoritos
    with open(caminho_favoritos, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha['usuário'] == usuario:
                favoritos.append({
                    "album_id": linha["album_id"],
                    "capa": linha["capa"]
                })
    return favoritos

#================================
def salvar_favorito(usuario, album_id, capa):
    inicializar_favoritos()

    fav = []
    with open(caminho_favoritos, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["usuário"] == usuario:
                fav.append(linha["album_id"])
    
    if album_id not in fav:
        with open(caminho_favoritos, "a", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([usuario, album_id, capa])

#==================================
def check_in_fav(album_id, usuario):
    with open(caminho_favoritos, 'r', newline='', encoding='utf-8') as arquivo:
        albuns_favs = csv.DictReader(arquivo)
        for linha in albuns_favs:
            if (linha['album_id'] == album_id) and (linha['usuário'] == usuario):
                return True
    return False

#============================================
#Mesma lógica da biblioteca
def remover_favorito(album_id, usuario):
    manter = []
    with open(caminho_favoritos, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if not(linha['album_id'] == album_id and linha['usuário'] == usuario):
                manter.append(linha)

    with open(caminho_favoritos, 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=['usuário', 'album_id', 'capa'])
        escritor.writeheader()
        escritor.writerows(manter)