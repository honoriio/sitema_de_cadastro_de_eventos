from modulos.bibliotecas.uuid import limpar_tela
from modulos.database.credenciais import CredenciaisUsuario
from modulos.interface.elemento import linha_dupla

def login():
    
    while True:
        linha_dupla()
        print('LOGIN EVENTHUB V-0.1.2'.center(86))
        linha_dupla()
        usuario = input('Insira seu email: ')
        senha = input('Insira sua senha: ')
        senha_armazenada = CredenciaisUsuario.credenciais('cadastro.db', usuario, senha)  # Obtem a senha armazenada
        if senha == senha_armazenada:
            break



