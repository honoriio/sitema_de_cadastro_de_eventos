# Modulo criado para agrupar as funções criadas para a criação de cadastro

# Area destinada para a inportação dos modulos necessarios


from modulos.validacao import validar_email
from modulos.validacoes_eventos import *


class evento:
    def __init__(self, titulo, descricao, data, hora_evento, local_evento, categoria, organizador, contato_evento, inscricao, custo):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.hora_evento = hora_evento
        self.local_evento = local_evento
        self.categoria = categoria
        self.organizador = organizador
        self.contato_evento = contato_evento
        self.inscricao = inscricao
        self.custo = custo


def cadastro_eventos():
    dados_evento = {}  # Dicionário para armazenar os dados do cadastro dos eventos, Para usarmos posteriormente no banco de dados.

    while True:
        try:
            titulo = input('Informe o titulo: ')
            if validar_titulo(titulo) and titulo.strip() != '':
                dados_evento['titulo'] = titulo
                break
            else:
                print('O titulo não pode estar em branco, Por favor, informe um titulo válido.')
        except ValueError:
            print('Erro ao processar o titulo, Certifique-se de inserir um valor válido.')
    while True:
        try:
            descricao = input('Informe uma breve descrição para o seu evento: ')
            if validar_titulo(descricao) and descricao.strip() != '':
                dados_evento['descricao'] = descricao
                break
            else:
                print('A descrição informada contem carcteres invalidos, por favor verifique os dados inseridos.')
        except ValueError:
            print('Erro ao processar os dados da descrição, por favor, insira valores validos.')
    while True:
        try:
            data_evento = input('Informe a data do evento (DD/MM/AAAA): ')
            if validar_data(data_evento):
                dados_evento['data_evento'] = data_evento
                break
            else:
                print('Data do evento inválida. Por favor, insira no formato correto (DD/MM/AAAA).')
        except ValueError:
            print('Erro ao processar a data do evento, Certifique-se de inserir um valor válido.')
    while True:
        try:
            hora_evento = input('Informe a horario do evento: ')
            if validar_hora(hora_evento):
                dados_evento['hora_evento'] = hora_evento
                break
            else:
                print('A hora para o evento informada e invalida, insíra um horaio valido dentro do formato: (HH:MM)')
        except ValueError:
            print('Erro ao processar o horario do evento, Por favor, insíra um valor valido.')

    # loop criado para coletar informações sobre o endereço do local do evento.
    while True:
        try:
            local_evento = input('Informe o local do evento: ')
            if validar_titulo(local_evento):
                dados_evento['local_evento'] = local_evento
                break
            else:
                print('O local do evento inserido esta invalido, Por favor, insira um local valido')
        except ValueError:
            print('O local informado contem caracteres invalidos, por favor insira somente letras e numeros.')
    while True:
        try:
            rua_evento = input('Informe o endereço do evento: ')
            if validar_titulo(rua_evento):
                dados_evento['endereco_evento'] = rua_evento
                break
            else:
                print('A rua informado e invaldo, por favor, insira um nome de rua valido.')
        except ValueError:
            print('A rua fornecido contem caracteres invalidos, por favor, use somente letras e números. ')
    while True:
        try:
            bairro_evento = input('Informe o bairro: ')
            if validar_titulo(bairro_evento):
                dados_evento['bairro_evento'] = bairro_evento
                break
            else:
                print('O bairro fonecido esta invalido, Por favor, infome um bairro valido.')
        except ValueError:
            print('O bairro infomado contem caracteres invalidos, Por favor, use somente letras e numeros.')
    while True:
        try:
            cidade_evento = input('Informe a cidade: ')
            if validar_titulo(cidade_evento):
                dados_evento['cidade_evento'] = cidade_evento
                break
            else:
                print('O nome da cidade informado esta incorreto, por favor, informe um nome valido.')
        except ValueError:
            print('O nome da cidade fornecido contem caracteres invalidos, por favor, Use somente letras e numeros.')
    while True:
        try:
            estado_evento = input('Informe o estado: ')
            if validar_estado(estado_evento):
                dados_evento['estado_evento'] = estado_evento
                break
            else:
                print('O estado informado é invalido, por favor informe um estado valido.')
        except ValueError:
            print('O estado informado contem caracteres invalidos, Por favor, insira somente letras.')
    while True:
        try:
            cep_evento = input('Informe o cep do evento: ')
            if validar_cep(cep_evento):
                dados_evento['cep_evento'] = cep_evento
                break
            else:
                print('O cep informado esta incorreto, Por favor, insira um cep valido.')
        except ValueError:
            print('O cep informado contem caracteres invalidos, por favor, insira somente numeros.')
    
    # Loop criado para a coleta de dados de cintatos do evento
    while True:
        try:
            contato_evento = input('Informe um numero para contato: ')
            if validar_telefone(contato_evento):
                dados_evento['contato_evento'] = contato_evento
                break
            else:
                print('O número informado e inválido, por favor verifique o número e tente novamente.')
        except ValueError:
            print('Erro ao validar o número de telefone informado, por favor verifique o número e tente novamente.')
    while True:
        try:
            email_evento = input('Informe seu melhor e-mail: ')
            if validar_email(email_evento):
                dados_evento['email_evento'] = email_evento
                break
            else: 
                print('O e-mail informado não é válido.')
        except ValueError:
            print('Erro ao validar e-mail, por favor informe um e-mail válido.')
    return dados_evento
