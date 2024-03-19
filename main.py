import sys
import time
from modulos.interface.elemento import *



menu()
print('[1]- Cadastrar um novo usuário.')
print('[2]- Cadastrar um novo evento.')
print('[3]- Login')
linha()

opc = input('opção: ')

if opc == '1':
    from modulos.database.data_base import BancoDeDados
    bd = BancoDeDados()
elif opc == '2':
    from modulos.funcoes_eventos import *
    from modulos.database.data_base_eventos import BancoDeDadosEventos
    from modulos.funcoes import *
    bd = BancoDeDadosEventos()
    linha()
elif opc == '3':
    from modulos.bibliotecas.uuid import limpar_tela
    limpar_tela()
    from modulos.funções_login import login
    resultado_login = login()
    if resultado_login == 1:
        print("Login bem-sucedido!")
        limpar_tela()
        menu()

        print('[1]- Vizualizar eventos cadastrados.')
        print('[2]- Vizualizar eventos inscritos.')
        print('[3]- Sair')
        linha()
        opc = input('opção: ')
        linha()

        if opc == '1':
            limpar_tela()
            menu()
            from modulos.database.print_data_base_eventos import PrintBancoDeDadosEventos
            PrintBancoDeDadosEventos()
            print('Deseja se inscrever em um evento?')
            opc = input('Opção: ')
        elif opc == '2':
            print('teste')

        elif opc == '3':
            print('Encerrando o programa...')
            time.sleep(2)
            limpar_tela()
            sys.exit()

            