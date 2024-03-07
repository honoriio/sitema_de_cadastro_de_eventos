# Local destinado para as importações necessarias para criação do programa
import sqlite3
from modulos.api.api import consulta_cep
from modulos.funcoes import cadastro

class BancoDeDados:
    # Função para conectar ao banco de dados
    def conectar(self, nome_banco):
        self.conn = sqlite3.connect(nome_banco)

    # Função para desconectar do banco de dados
    def desconectar(self):
        self.conn.close()

    # Função para criar a tabela no banco de dados
    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pessoas(
                id INTEGER PRIMARY KEY,
                nome TEXT,
                data_nascimento TEXT,
                email TEXT,
                sexo TEXT,
                cep TEXT,
                uf TEXT,
                logradouro TEXT,
                complemento TEXT
            )
        ''')
        self.conn.commit()

    # Função para inserir os dados do dicionário na tabela
    def inserir_dados(self, dados):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO pessoas (nome, data_nascimento, email, sexo, cep, uf, logradouro, complemento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (dados['nome'], dados['data_nascimento'], dados['email'], dados['sexo'], dados['cep'], dados['uf'], dados['logradouro'], dados['complemento']))
        self.conn.commit()

    # Função para processar o cadastro
    def processar_cadastro(self):
        # Obtém os dados do cadastro
        cep, dados = cadastro()

        # Consulta o CEP
        cep_info = consulta_cep(cep)

        if cep_info:
            dados.update(cep_info)  # Adiciona os dados do CEP ao dicionário de dados de cadastro

            # Conecta ao banco de dados
            self.conectar('cadastro.db')

            # Cria a tabela se ainda não existir
            self.criar_tabela()

            # Insere os dados na tabela
            self.inserir_dados(dados)

            # Desconecta do banco de dados
            self.desconectar()
        else:
            print("CEP não encontrado.")

# Instanciando a classe BancoDeDados e chamando o método processar_cadastro
bd = BancoDeDados()
bd.processar_cadastro()
