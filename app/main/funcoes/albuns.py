import csv, os

os.makedirs("data", exist_ok=True)

caminho_album = 'data/albuns.csv'
caminho_musicas = 'data/musicas.csv'
caminho_review = 'data/review.csv'


#=================================FUNÇÕES===================================

  #CRIAR OS ALBUNS

id_automatico_album = 1
def salvar_album(capa,nome,lancamento,genero,artista,foto_bio,biografia,spotify):

    global id_automatico_album

    dados = []
    album = []
    album.append(id_automatico_album)
    album.append(capa)
    album.append(nome)
    album.append(lancamento)
    album.append(genero)
    album.append(artista)
    album.append(foto_bio)
    album.append(biografia)
    album.append(spotify)
    dados.append(album)

    id_automatico_album += 1

# AQUI ELE VERIFICA SE O ARQUIVO EXISTE, CASO NÃO ELE CRIA
    if not os.path.exists(caminho_musicas):
        with open(caminho_album, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerow(['album_id','capa','nome','lancamento','genero','artista','foto_bio','biografia','spotify'])
            escritor.writerows(dados)

    else: 
        with open(caminho_album, "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerows(dados)



#=========================================
id_automatico_musicas = 1

def salvar_musicas(musicas):
    global id_automatico_musicas
    colecao = []
    faixas = []
    musica = musicas.strip().split(';')
    faixas.append(id_automatico_musicas)
    faixas.append(musica)
    colecao.append(faixas)

    id_automatico_musicas += 1

# AQUI ELE VERIFICA SE O ARQUIVO EXISTE, CASO NÃO ELE CRIA
    if not os.path.exists(caminho_musicas):
        with open(caminho_musicas, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerow(['album_id','musicas'])
            escritor.writerows(colecao)

    else:
        with open(caminho_musicas, "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerows(colecao)

#==========================================
def salvar_comentario (album_id,review):

    comentario = []
    lista_info = []
    lista_info.append(album_id)
    lista_info.append([review])
    comentario.append(lista_info)

# AQUI ELE VERIFICA SE O ARQUIVO EXISTE, CASO NÃO ELE CRIA
    if not os.path.exists(caminho_review):
        with open(caminho_review, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerow(['album_id','review'])
            escritor.writerows(comentario)
    else:
         with open(caminho_review, "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq, delimiter=';')
            escritor.writerows(comentario)


#teste para cadastro==============================================
#capa: https://cdn-images.dzcdn.net/images/cover/379aa0302d0df5bdd9e4a01829ca36d6/500x500-000000-80-0-0.jpg
# nome: Sonder Son
# lancamento: 2017
# genero: R&B
# artista: Brent Faiyaz
# foto_bio: https://i.pinimg.com/736x/cc/09/f9/cc09f900551c455b82d29977282d8675.jpg
# biografia: Brent Wood, conhecido como Brent Faiyaz, é um cantor e compositor americano de Columbia, Maryland,
# que ganhou destaque com Crew (2016) e lançou o debut Sonder Son em 2017, marcado por R&B atmosférico e letras introspectivas.
# musicas: Over Luv;Burn One (Interlude);First World Problemz/Nobody Carez;Missing Out;Stay
# Down;L.A.;Talk 2 U;Sonder Son (Interlude);So Far Gone/Fast Life Bluez;Needed;All I Want
 
#==========================================================
# AQUI ELE LÊ OS ARQUIVOS CSV
def carregar_album():
    arq_album = open(caminho_album,'r', encoding='utf-8')
    linhas_album = csv.DictReader(arq_album, delimiter=";") 
    album = []
    for linha in linhas_album:
        album.append(linha)
    arq_album.close()
    return album

#============================================
def carregar_discografia()->list:
    arq_musicas = open(caminho_musicas,'r', encoding='utf-8')
    linhas_musicas = csv.DictReader(arq_musicas, delimiter=";")
    faixas = []
    for m in linhas_musicas:
            musicas = m
            faixas.append(musicas)
    arq_musicas.close()
    return musicas

#=========================================
def carregar_discografia(album_id) -> list:
    with open(caminho_musicas, 'r', encoding='utf-8') as arq_musicas:
        leitor = csv.DictReader(arq_musicas, delimiter=";")
        for m in leitor:
            if m['album_id'] == str(album_id):
                # remove colchetes
                musicas_str = m['musicas'].strip('[]')
                # separa corretamente por vírgula e limpa aspas/espacos
                faixas = [item.strip().strip("'").strip('"') for item in musicas_str.split(",")]
    return faixas

#=======================================
def carregar_review()->list:
    arq_review = open(caminho_review, 'r')
    linhas_review = csv.DictReader(arq_review, delimiter=";")
    comentarios = []
    for c in linhas_review:
            review = c
            comentarios.append(review)
    arq_review.close()
    return comentarios

# AQUI ELE COMPARA OS IDS

def comparar_id (album_id):
    albuns = carregar_album()
    for album in albuns:
        if album['album_id'] == str(album_id):
            return album
    return None
