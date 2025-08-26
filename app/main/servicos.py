import csv, os

os.makedirs("data", exist_ok=True)

caminho_album = 'data/albuns.csv'
caminho_musicas = 'data/musicas.csv'
caminho_review = 'data/review.csv'

id = 0

#   #CRIAR OS ALBUNS
# NO LUGAR DOS INPUTS COLOCAR OS FORMULARIOS
def salvar_album(capa,nome,lancamento,genero,artista,foto_bio,biografia,spotify):
    # global id += 1
    dados = [['album_id','capa','nome','lancamento','genero','artista','foto_bio','biografia''spotify']]
    album = []
    album.append(id)
    album.append(capa)
    album.append(nome)
    album.append(lancamento)
    album.append(genero)
    album.append(artista)
    album.append(foto_bio)
    album.append(biografia)
    album.append(spotify)
    dados.append(album)

    with open(caminho_album, "a", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq, delimiter=';')
        escritor.writerows(dados)

    return dados


def salvar_musicas(album_id,musicas):
    colecao = [['album_id','musicas']]
    faixas = []
    musica = musicas.strip().split(';')
    faixas.append(album_id)
    faixas.append(musica)
    colecao.append(faixas)

    with open(caminho_musicas, "a", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq, delimiter=';')
        escritor.writerows(colecao)



# with open(caminho_review, "w", newline="", encoding="utf-8") as arq:
#     escritor = csv.writer(arq, delimiter=';')
#     escritor.writerows(colecao)


# def musicas(id,musicas):
#     colecao = [["album_id","musicas" ]]
#     faixas = []
#     for m in musicas:
#          musica = m.strip().split(';')
#          faixas.append(musica)
#     colecao.append(id)
#     colecao.append(faixas)

#     with open(caminho_musicas, "a", newline="", encoding="utf-8") as arq:
#         escritor = csv.writer(arq, delimiter=';')
#         colecao = musicas(id,musicas)
#         escritor.writerows(colecao)

# comentarios = [["id_album", "comentario"]]
# while True:



  #trocar o 'w' pelo 'a' quando for usar de verdade

# with open(caminho_review, "w", newline="", encoding="utf-8") as arq:
#     escritor = csv.writer(arq, delimiter=';')
#     escritor.writerows(colecao)

  #LER O ARQUIVO CSV ONDE ESTÁ A LISTA DE ALBUNS
# AQUI A FUNÇÃO VAI RECEBER OS VALORES E COLOCAR EM UM DIC PARA FICAR MAIS FACIL PRA SUBSTITUIR
def carregar_album():
    arq_album = open(caminho_album,'r', encoding='utf-8')
    lista_albuns = []
    linhas_album = csv.DictReader(arq_album, delimiter=";")  
    for linha in linhas_album:
        album = {
            'album_id': linha['album_id'],
            'capa': linha['capa'],
            'nome': linha['nome'],
            'lancamento': linha['lancamento'],
            'genero': linha['genero'],
            'artista': linha['artista'],
            'foto_bio': linha['foto_bio'],
            'biografia': linha['biografia'],
            'spotify': linha['spotify']
            }
        lista_albuns.append(album)
    arq_album.close()

    return lista_albuns

def carregar_discografia()->list:
    arq_musicas = open(caminho_musicas,'r', encoding='utf-8')
    linhas_musicas = arq_musicas.readlines()
    faixas = []
    for l in linhas_musicas[1:]:
            musicas = l.strip().split(';')
            faixas.append(musicas)
    arq_musicas.close()  

    return musicas




# lista_albuns = carregar_album()

# for d in lista_albuns:
#      if d['id'] == album_id :
#             return f"<h1>{album['nome']}</h1><img src='{album['img']}' />"
#      return "Álbum não encontrado"
