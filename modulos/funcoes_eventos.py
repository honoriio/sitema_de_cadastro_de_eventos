# Modulo criado para agrupar as funções criadas para a criação de cadastro

class evento:
    def __init__(self, titulo, descricao, data, hora, local, categoria, organizador, contato, inscricao, custo):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.local = local
        self.categoria = categoria
        self.organizador = organizador
        self.contato = contato
        self.inscricao = inscricao
        self.custo = custo


def cadastro_eventos():
    dados_eventos = {} # Dicionario criado para armazenar os dados adquiridos que usaremos posteriormente.
    
