from app.main.funcoes.albuns import carregar_album  

# Associa anos com values do checkbox
def classificar_decada(lancamento):
    lancamento = lancamento.strip()
    if lancamento.isdigit():
        lancamento = int(lancamento)
        
        if 2020 <= lancamento <= 2025:
            return '20s'
        elif 2010 <= lancamento <= 2019:
            return '10s'
        elif 2000 <= lancamento <= 2009:
            return '00s'
        elif 1990 <= lancamento <= 1999:
            return '90s'
        elif 1980 <= lancamento <= 1989:
            return '80s'
        elif 1970 <= lancamento <= 1979:
            return '70s'
    return None

albuns = carregar_album()

def filtrar_albuns(albuns, generos, lancamentos):
    filtrados = []
    for alb in albuns:
        genero = alb.get('generos', '').strip()
        lancamento = alb.get('lancamento', '')
        decada = classificar_decada(lancamento)

# aceita o álbum se o usuário não escolheu nenhum gênero/lançamento ou o gênero/lançamento do álbum está na lista escolhida
        genero_ok = not generos or genero in generos
        lancamento_ok = not lancamentos or decada in lancamentos

        if genero_ok and lancamento_ok:
            filtrados.append(alb)
    return filtrados
