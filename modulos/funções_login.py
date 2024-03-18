from modulos.database.credenciais import CredenciaisUsuario
from modulos.interface.elemento import linha_dupla

def login():
    linha_dupla()
    print('LOGIN EVENTHUB V-0.1.2'.center(86))
    linha_dupla()
    usuario = input('Insira seu email: ')
    senha = input('Insira sua senha: ')
    
    # Verifica as credenciais do usuário
    pb = CredenciaisUsuario()
    pb.credenciais('cadastro.db', usuario, senha)


