import csv, os

os.makedirs("data", exist_ok=True)

caminho_album = 'data/albuns.csv'
caminho_musicas = 'data/musicas.csv'
caminho_review = 'data/review.csv'

id_automatico = 1
#   #CRIAR OS ALBUNS
# NO LUGAR DOS INPUTS COLOCAR OS FORMULARIOS
def salvar_album(capa,nome,lancamento,genero,artista,foto_bio,biografia,spotify):

    global id_automatico

    dados = []
    album = []
    album.append(id_automatico)
    album.append(capa)
    album.append(nome)
    album.append(lancamento)
    album.append(genero)
    album.append(artista)
    album.append(foto_bio)
    album.append(biografia)
    album.append(spotify)
    dados.append(album)

    id_automatico += 1


    if not os.path.exists(caminho_musicas):
        with open(caminho_album, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerows(['capa','nome','lancamento','genero','artista','foto_bio','biografia','spotify'])

        
        with open(caminho_album, "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerows(dados)

    return dados

def salvar_musicas(musicas):

    global id_automatico

    colecao = []
    faixas = []
    musica = musicas.strip().split(';')
    faixas.append(id_automatico)
    faixas.append(musica)
    colecao.append(faixas)

    id_automatico += 1

    if not os.path.exists(caminho_musicas):
        with open(caminho_musicas, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerows(['album_id','musicas'])

    else:
        with open(caminho_musicas, "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerows(colecao)


def salvar_comentario (album_id,review):

    verificar = carregar_review()

    # for i in range(len(verificar)):
    #     if verificar['album_id'] == (album_id)

# TERMINAR DE VERIFICAR SE JÁ EXISTE ALGUMA REVIEW NO MESMO ID, PARA COLOCAR TUDO NA MESMA LISTA

    comentario = []
    lista_info = []
    lista_info.append(album_id)
    lista_info.append([review])
    comentario.append(lista_info)

    if not os.path.exists(caminho_review):
        with open(caminho_review, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerows(['album_id','review'])
            print(album_id)
    else:
         with open(caminho_review, "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerows(comentario)
            print(album_id)

     

  #LER O ARQUIVO CSV ONDE ESTÁ A LISTA DE ALBUNS
# AQUI A FUNÇÃO VAI RECEBER OS VALORES E COLOCAR EM UM DIC PARA FICAR MAIS FACIL PRA SUBSTITUIR
def carregar_album():
    arq_album = open(caminho_album,'r', encoding='utf-8')
    linhas_album = csv.DictReader(arq_album, delimiter=";") 
    album = []
    for linha in linhas_album:
        album.append(linha)
    arq_album.close()
    return album

def carregar_discografia(album_id)->list:
    arq_musicas = open(caminho_musicas,'r', encoding='utf-8')
    linhas_musicas = csv.DictReader(arq_musicas, delimiter=";")
    faixas = []
    for m in linhas_musicas:
            if m['album_id'] == str(album_id):
                m['musicas'] = m['musicas'].strip('[]')
                lista = [item.strip().strip("'").strip('"') for item in m['musicas'].split(";")]
                faixas.append({
                    'album_id': m['album_id'],
                    'musicas': lista
                })
    arq_musicas.close()
    print(faixas)
    return faixas


def carregar_review()->list:
    arq_review = open(caminho_review, 'r')
    linhas_review = csv.DictReader(arq_review, delimiter=";")
    comentarios = []
    for c in linhas_review:
            review = c
            comentarios.append(review)
    arq_review.close()
    print(comentarios)
    return comentarios



# for d in lista_albuns:
#      if d['id'] == album_id :
#             return f"<h1>{album['nome']}</h1><img src='{album['img']}' />"
#      return "Álbum não encontrado"
