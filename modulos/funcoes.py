# Area destinada para importação dos moculos necessarios

from modulos.validacao import *

class pessoa:
    def __init__(self,primeiro_nome, sobrenome, nascimento, sexo, endereco, cep):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self. nascimento = nascimento
        self.sexo = sexo
        self.endereco = endereco
        self.cep = cep



def cadastro():
    # Loop criado para a entrada do campo nome, aqui vamos verificar se, o usúario inseriu apenas letras e os acentos validos
    # os caracteres permitidos estão todos descriminados na função validar_nome na pasta modulos/

    while True:
        try:
            nome = input('Informe o nome: ')
            if validar_nome(nome) and nome.strip() != '':
                break
            else:
                print('O Nome não pode estar em branco, Por favor, informe um nome válido.')
        except ValueError:
            print('Erro ao processar o nome, Certifique-se de inserir um valor válido.')
    while True:
        try:
            nascimento = input('Informe a data de nascimento: ')
            if validar_data(nascimento):
                break
        except ValueError:
            print('Erro ao processar a data de nascimento, Certifique-se de inserir um valor válido.')
    while True:
        try:
            email = input('Informe seu melhor e-mail: ')
            if validar_email(email):
                break
            else: 
                print('P e-mail informado não e valido.')
        except ValueError:
            print('Erro ao validar e-mail, por favor informe um e-mail valido.')