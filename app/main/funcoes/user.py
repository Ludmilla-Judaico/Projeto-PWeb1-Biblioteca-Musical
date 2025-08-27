from flask import session
import csv, os
#==================FUNÇÕES====================
caminho_usuarios = "data/usuarios.csv"

def signin(user, email, senha):
    if not os.path.exists(caminho_usuarios):
        with open(caminho_usuarios, 'w', newline="", encoding="utf-8") as arquivo_user:
            writer = csv.writer(arquivo_user)
            writer.writerow(['usuário', 'email', 'senha', 'foto'])

    foto = 'static/imgs/perfil-default.png'
    with open(caminho_usuarios, 'a', newline="", encoding="utf-8") as arquivo_user:
        writer = csv.writer(arquivo_user)
        writer.writerow([user, email, senha, foto])

#==============================
def dados_associados(user_email):          
    with open(caminho_usuarios, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["email"] == user_email:
                nome = linha['usuário']
                foto = linha['foto']
                return nome, foto
            
#===============================            
def authenticator(user_email, senha):
    if os.path.exists(caminho_usuarios):
        with open(caminho_usuarios, newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if (linha['email'] == user_email) and (linha['senha'] == senha):
                    return True
            return False
    return False
            
#===============================
def edit_user(novo_usuario=None, novo_email=None, nova_senha=None, nova_foto=None):
    with open(caminho_usuarios, "r", newline="", encoding="utf-8") as arquivo:
        linhas = []
        leitor = csv.DictReader(arquivo)
        dados = leitor.fieldnames
        for linha in leitor:
            if session['usuario'] == linha['usuário']:
                if novo_usuario:
                    linha['usuário'] = novo_usuario
                if novo_email:
                    linha['email'] = novo_email
                if nova_senha:
                    linha['senha'] = nova_senha
                if nova_foto:
                    linha['foto'] = nova_foto
            linhas.append(linha)

    with open(caminho_usuarios, "w", newline="", encoding="utf-8") as arquivo:
        
        escritor = csv.DictWriter(arquivo, fieldnames=dados)
        escritor.writeheader()
        escritor.writerows(linhas)

    if novo_usuario:
        session['usuario'] = novo_usuario
    if novo_email:
        session['email'] = novo_email
    if nova_foto:
        session['foto'] = nova_foto