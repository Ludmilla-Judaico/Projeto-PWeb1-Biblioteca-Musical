import csv, os
caminho_biblioteca = 'data/biblioteca.csv'

#=======================FUNÇÕES==========================
#==================================================
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

#==========================================================
#caso o csv da biblioteca não exista
def inicializar_biblioteca():
    if not os.path.exists(caminho_biblioteca):
        os.makedirs(os.path.dirname(caminho_biblioteca), exist_ok=True)
        with open(caminho_biblioteca, "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["usuário", "album_id", "capa"])

#======================================================
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

#=====================================================
#checa se o album ja está na biblioteca do usuario
def check_in_biblioteca(album_id, usuario):
    with open(caminho_biblioteca, 'r', newline='', encoding='utf-8') as arquivo:
        minha_biblioteca = csv.DictReader(arquivo)
        for linha in minha_biblioteca:
            if (linha['album_id'] == album_id) and (linha['usuário'] == usuario):
                return True
    return False

#=========================================================
#Lê o arquivo csv da biblioteca e itera por todas as linhas do arquivo, colocando todas em uma lista. 
#Se ele achar o id do álbum no csv, ele pula essa linha e não coloca ele na lista
#Ao final ele reescreve o arquivo utilizando essa lista que não possui a linha do álbum que desejava remover
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