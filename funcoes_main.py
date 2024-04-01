import sys
import time
from modulos.interface.elemento import *

def cadastrar_usuario():
    from modulos.database.data_base import BancoDeDados
    bd = BancoDeDados()

def cadastrar_evento():
    from modulos.funcoes_eventos import menu
    from modulos.database.data_base_eventos import BancoDeDadosEventos
    from modulos.funcoes import cadastro
    bd = BancoDeDadosEventos()
    linha()

def fazer_login():
    from modulos.bibliotecas.uuid import limpar_tela
    limpar_tela()
    from modulos.funções_login import login
    resultado_login = login()
    if resultado_login == 1:
        print("Login bem-sucedido!")
        limpar_tela()

def visualizar_eventos():
    from modulos.bibliotecas.uuid import limpar_tela
    limpar_tela()
    menu()
    from modulos.database.print_data_base_eventos import PrintBancoDeDadosEventos
    PrintBancoDeDadosEventos()

def visualizar_eventos_para_inscricao():
    from modulos.database.eventos_com_inscricao import PrintEventosInscricao
    PrintEventosInscricao()
    print('[1]- Cadastrar no evento.')
    print('[2]- Voltar pagina.')

def encerrar_programa():
    from modulos.bibliotecas.uuid import limpar_tela
    print('Encerrando o programa...')
    time.sleep(2)
    limpar_tela()
    sys.exit()

def menu_login():
    menu()
    print('[1]- Cadastrar um novo usuário.')
    print('[2]- Cadastrar um novo evento.')
    print('[3]- Login')
    linha()

    opc = input('opção: ')

    if opc == '1':
        cadastrar_usuario()
    elif opc == '2':
        cadastrar_evento()
    elif opc == '3':
        fazer_login()

def menu_login2():
    menu()
    print('[1]- Vizualizar eventos cadastrados.')
    print('[2]- Vizualizar eventos para Inscrição.')
    print('[3]- Vizualizar eventos inscritos.')
    print('[4]- Sair')
    linha()
    opc = input('opção: ')
    linha()

    if opc == '1':
        visualizar_eventos()
    elif opc == '2':
        visualizar_eventos_para_inscricao()
    elif opc == '4':
        encerrar_programa()

