import time
from modulos.bibliotecas.uuid import limpar_tela
from modulos.database.credenciais import CredenciaisUsuario
from modulos.interface.elemento import linha_dupla

def login():
    cont = 0 
    while True:
        linha_dupla()
        print('LOGIN EVENTHUB V-0.1.2'.center(86))
        linha_dupla()
        usuario = input('Insira seu email: ')
        senha = input('Insira sua senha: ')
        senha_armazenada = CredenciaisUsuario.credenciais('cadastro.db', usuario, senha)  # Obtem a senha armazenada
        cont = cont + 1
        if cont == 2:
            print('')
            tempo_inicio = time.time()
            for segundos_restantes in range(180, 0, -1):  # Contagem regressiva de 180 a 1 segundo
                minutos = segundos_restantes // 60
                segundos = segundos_restantes % 60
                linha_dupla()
                print('LOGIN EVENTHUB V-0.1.2'.center(86))
                linha_dupla()
                print(f'Varias tentativas de login sem sucesso, tente novamente em 3 minutos, Tempo restante: {minutos:02d}:{segundos:02d}', end='\r')
                time.sleep(1)
                limpar_tela()
        if senha == senha_armazenada:
            break




