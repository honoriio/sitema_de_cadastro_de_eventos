from modulos.database.data_base import BancoDeDados
from modulos.funcoes import *
from modulos.api.api import imprimir_informacoes_cep

cep, dados = cadastro()
imprimir_informacoes_cep(cep)
