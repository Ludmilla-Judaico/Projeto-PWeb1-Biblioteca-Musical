import csv

  #CRIAR OS ALBUNS

dados = [["id","capa", "nome", "lancamento", "genero", "artista", "biografia"]]
while True:
     album = []
     id = input('id: ')
     if id == 'FIM':
         break
     album.append(input('Capa: '))
     album.append(input('Nome do album: '))
     album.append(input('Lançamento: '))
     album.append(input('Gênero: '))
     album.append(input('Artista: '))
     album.append(input('Biografia: '))
     dados.append(album)

  #trocar o 'w' pelo 'a' quando for usar de verdade

with open("albuns.csv", "w", newline="", encoding="utf-8") as arq:
     escritor = csv.writer(arq, delimiter=';')
     escritor.writerows(dados)

  #LER O ARQUIVO CSV ONDE ESTÁ A LISTA DE ALBUNS

def carregar_album()->list:
     arq = open('albuns.csv','r', encoding='utf-8')
     lista_albuns = []
     linhas = arq.readlines()
     for linha in linhas[1:]:
         id,capa,nome,lancamento,genero,artista,biografia = linha.strip().split(';')
         album = {
             'id': id,
             'capa': capa,
             'nome': nome,
             'lancamento': lancamento,
             'genero':genero,
             'artista': artista,
             'biografia': biografia
             }
         lista_albuns.append(album)
     arq.close()
     return lista_albuns


# lista_albuns = carregar_album()

# for d in lista_albuns:
#      if d['id'] == album_id :
#             return f"<h1>{album['nome']}</h1><img src='{album['img']}' />"
#      return "Álbum não encontrado"
