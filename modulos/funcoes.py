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

    # Loop criado para a entrada e verficação dos dados inseridos pelo usuario no campo de data de nascimento
    while True:
        try:
            nascimento = input('Informe a data de nascimento: ')
            if validar_data(nascimento):
                break
        except ValueError:
            print('Erro ao processar a data de nascimento, Certifique-se de inserir um valor válido.')

    # Loop criado para a entrada do campo email e para a validação dos dados inseridos pelo usuario
    while True:
        try:
            email = input('Informe seu melhor e-mail: ')
            if validar_email(email):
                break
            else: 
                print('O e-mail informado não e valido.')
        except ValueError:
            print('Erro ao validar e-mail, por favor informe um e-mail valido.')
    
    # Loop criado para a entrad do campo sexo e para a validação do mesmo.
    while True:
        try:
            print('Qual o seu sexo?')
            print('[1]- Masculino')
            print('[2]- Feminino')
            sexo = leiaint('Opção: ')
            if sexo == 1 or sexo == 2:
                break
            else:
                print('A opção escolhida esta incorreta, insira uma opção valida.')
        except ValueError:
            print('Erro ao validar o campo sexo, por favor informe uma opção valida.')
    
    # Loop criado para a entrada do campo cep e para a validação dos dados inseridos pelo usuario.
    while True:
        try:
            cep = input('Informe o CEP de 8 digitos: ')
            if validar_cep(cep):
                break
            else:
                print('O CEP informado e invalido.')
        except ValueError:
            print('Erro ao validar o CEP, Por favor verifique os dados informados e digite novamente.')
    return cep
