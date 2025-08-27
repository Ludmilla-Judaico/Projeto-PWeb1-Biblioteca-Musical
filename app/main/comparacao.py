from .servicos import carregar_album, carregar_discografia, carregar_review

def comparar_id (album_id):
    albuns = carregar_album()
    for album in albuns:
        if album['album_id'] == str(album_id):
            return album
    return None

def comparar_discografia(album_id):
        musicas = carregar_discografia()
        for m in musicas:
             if m['album_id'] == str(album_id):
                  return m
        return None