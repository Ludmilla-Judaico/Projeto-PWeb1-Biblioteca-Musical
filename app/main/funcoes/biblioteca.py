import csv, os
caminho_biblioteca = 'data/biblioteca.csv'

def carregar_biblioteca(usuario):
    minha_biblioteca = []
    if not os.path.exists(caminho_biblioteca):
        return minha_biblioteca
    with open(caminho_biblioteca, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha['usuário'] == usuario:
                minha_biblioteca.append({
                    "album_id": linha["album_id"],
                    "capa": linha["capa"]
                })
    return minha_biblioteca

def inicializar_biblioteca():
    if not os.path.exists(caminho_biblioteca):
        os.makedirs(os.path.dirname(caminho_biblioteca), exist_ok=True)
        with open(caminho_biblioteca, "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["usuário", "album_id", "capa"])

def salvar_na_biblioteca(usuario, album_id, capa):
    inicializar_biblioteca()

    album = []
    with open(caminho_biblioteca, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["usuário"] == usuario:
                album.append(linha["album_id"])
    
    if album_id not in album:
        with open(caminho_biblioteca, "a", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([usuario, album_id, capa])

def check_in_biblioteca(album_id, usuario):
    with open(caminho_biblioteca, 'r', newline='', encoding='utf-8') as arquivo:
        minha_biblioteca = csv.DictReader(arquivo)
        for linha in minha_biblioteca:
            if (linha['album_id'] == album_id) and (linha['usuário'] == usuario):
                return True
    return False

def remover_da_biblioteca(album_id):
    manter = []
    with open(caminho_biblioteca, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if not(linha['album_id'] == album_id):
                manter.append(linha)

    with open(caminho_biblioteca, 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=['usuário', 'album_id', 'capa'])
        escritor.writeheader()
        escritor.writerows(manter)