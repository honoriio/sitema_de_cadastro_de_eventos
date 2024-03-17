# Local destinado para a importação de modulos e bibliotecas 
import uuid
import os

def gerar_uuid():
    return str(uuid.uuid4())



def limpar_tela():
    # Verifica o sistema operacional
    if os.name == 'posix':  # Linux e macOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')


