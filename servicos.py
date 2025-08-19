import csv

#   #CRIAR OS ALBUNS
dados = [["id","capa", "nome", "lancamento", "genero", "artista", "foto_bio", "biografia", "spotify"]]
colecao = [["album_id","musicas" ]]
while True:
    id = input('id: ')
    album = []
    musicas = []
    if id == 'FIM':
        break
    album.append(id)
    album.append(input('Capa: '))
    album.append(input('Nome do album: '))
    album.append(input('Lançamento: '))
    album.append(input('Gênero: '))
    album.append(input('Artista: '))
    album.append(input('Foto da bio: '))
    album.append(input('Biografia: '))
    album.append(input('link do spotify: '))
    dados.append(album)

    qtd_repeticoes = int(input("Qual a quantidade de músicas: "))
    lista_musicas = []
    for i in range(qtd_repeticoes):
        musica = input('qual a música: ')
        lista_musicas.append(musica)
    musicas.append(id)
    musicas.append(lista_musicas)
    colecao.append(musicas)

  #trocar o 'w' pelo 'a' quando for usar de verdade
with open("albuns.csv", "w", newline="", encoding="utf-8") as arq:
    escritor = csv.writer(arq, delimiter=';')
    escritor.writerows(dados)

with open("discografia.csv", "w", newline="", encoding="utf-8") as arq:
    escritor = csv.writer(arq, delimiter=';')
    escritor.writerows(colecao)

  #LER O ARQUIVO CSV ONDE ESTÁ A LISTA DE ALBUNS

def carregar_album()->list:
    arq_album = open('albuns.csv','r', encoding='utf-8')
    lista_albuns = []
    linhas_album = arq_album.readlines()  
    for linha in linhas_album[1:]:
        id,capa,nome,lancamento,genero,artista,foto_bio,biografia,spotify = linha.strip().split(';')
        album = {
            'id': id,
            'capa': capa,
            'nome': nome,
            'lancamento': lancamento,
            'genero':genero,
            'artista': artista,
            'foto_bio': foto_bio,
            'biografia': biografia,
            'spotify': spotify
            }
        lista_albuns.append(album)
    arq_album.close()
    

    arq_musicas = open('discografia.csv','r', encoding='utf-8')
    linhas_musicas = arq_musicas.readlines()
    for l in linhas_musicas[1:]:
            id,musicas = l.strip().split(';')
            lista_albuns.append({
                'id': id,
                'musicas': musicas
            })
    arq_musicas.close()          

    return lista_albuns


a = carregar_album()
for l in a:
  print(l)




# lista_albuns = carregar_album()

# for d in lista_albuns:
#      if d['id'] == album_id :
#             return f"<h1>{album['nome']}</h1><img src='{album['img']}' />"
#      return "Álbum não encontrado"
