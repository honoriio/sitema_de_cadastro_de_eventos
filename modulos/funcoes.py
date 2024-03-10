# Modulos criado para agurapar as funções criadas para o cadastro de pessoas


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
    dados = {}  # Dicionário para armazenar os dados do cadastro, Para usarmos posteriormente no banco de dados.

    while True:
        try:
            nome = input('Informe o nome: ')
            if validar_nome(nome) and nome.strip() != '':
                dados['nome'] = nome
                break
            else:
                print('O Nome não pode estar em branco, Por favor, informe um nome válido.')
        except ValueError:
            print('Erro ao processar o nome, Certifique-se de inserir um valor válido.')

    while True:
        try:
            nascimento = input('Informe a data de nascimento (DD/MM/AAAA): ')
            if validar_data(nascimento):
                dados['data_nascimento'] = nascimento
                break
            else:
                print('Data de nascimento inválida. Por favor, insira no formato correto (DD/MM/AAAA).')
        except ValueError:
            print('Erro ao processar a data de nascimento, Certifique-se de inserir um valor válido.')
    while True:
        try:
            celular = input('Informe um numero para contato: ')
            if validar_telefone(celular):
                dados['numero_telefone'] = celular
                break
            else:
                print('O número informado e inválido, por favor verifique o número e tente novamente.')
        except ValueError:
            print('Erro ao validar o número de telefone informado, por favor verifique o número e tente novamente.')
    while True:
        try:
            email = input('Informe seu melhor e-mail: ')
            if validar_email(email):
                dados['email'] = email
                break
            else: 
                print('O e-mail informado não é válido.')
        except ValueError:
            print('Erro ao validar e-mail, por favor informe um e-mail válido.')
    
    while True:
        try:
            print('Qual o seu sexo?')
            print('[1]- Masculino')
            print('[2]- Feminino')
            sexo = leiaint('Opção: ')
            if sexo == 1:
                dados['sexo'] = 'Masculino'
                break
            elif sexo == 2:
                dados['sexo'] = 'Feminino'
                break
            else:
                print('Opção inválida. Por favor, insira 1 para Masculino ou 2 para Feminino.')
        except ValueError:
            print('Erro ao validar o campo sexo, por favor informe uma opção válida.')
    
    while True:
        try:
            cep = input('Informe o CEP de 8 dígitos: ')
            if validar_cep(cep):
                dados['cep'] = cep
                break
            else:
                print('O CEP informado é inválido. Por favor, insira um CEP válido.')
        except ValueError:
            print('Erro ao validar o CEP, Por favor verifique os dados informados e digite novamente.')
    
    return cep, dados
