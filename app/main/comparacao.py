import csv
from .servicos import carregar_album

def comparar_id (album_id):
    albuns = carregar_album()
    for album in albuns:
        if album['album_id'] == str(album_id):
            return album
    return None