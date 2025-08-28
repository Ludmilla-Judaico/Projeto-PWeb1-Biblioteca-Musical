from app.main.funcoes.albuns import carregar_album  # importe a função aqui

# Compara com os values do checkbox
def classificar_decada(ano):
    ano = ano.strip()
    if ano.isdigit():
        ano = int(ano)
        if 2020 <= ano <= 2025:
            return '20s'
        elif 2010 <= ano <= 2019:
            return '10s'
        elif 2000 <= ano <= 2009:
            return '00s'
        elif 1990 <= ano <= 1999:
            return '90s'
        elif 1980 <= ano <= 1989:
            return '80s'
        elif 1970 <= ano <= 1979:
            return '70s'
    return None

albuns = carregar_album()

def filtrar_albuns(albuns, generos, lancamentos):
    filtrados = []
    for alb in albuns:
        genero = alb.get('genero', '').lower()
        ano = alb.get('ano', '')
        decada = classificar_decada(ano)

# aceita o álbum se o usuário não escolheu nenhum gênero/lançamento ou o gênero/lançamento do álbum está na lista escolhida
        genero_ok = not generos or genero in generos
        lancamento_ok = not lancamentos or decada in lancamentos

        if genero_ok and lancamento_ok:
            filtrados.append(alb)
    return filtrados
