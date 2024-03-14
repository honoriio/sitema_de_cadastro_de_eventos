# Local destinado para as importações necessarias para criação do programa
import sqlite3

from modulos.funcoes_eventos import cadastro_eventos

class BancoDeDadosEventos:
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
            CREATE TABLE IF NOT EXISTS eventos(
                id INTEGER PRIMARY KEY,
                titulo TEXT,
                descricao TEXT,
                data TEXT,
                hora_evento TEXT,
                local_evento TEXT,
                categoria TEXT,
                organizador TEXT,
                contato_evento TEXT,
                inscricao TEXT,
                custo TEXT,
                rua_evento TEXT,
                bairro_evento TEXT,
                cidade_evento TEXT,
                estado_evento  TEXT,
                cep_evento TEXT,
                email_evento TEXT,
                id_evento TEXT
            )
        ''')
        self.conn.commit()

    def inserir_dados(self, dados_evento):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO eventos (titulo, descricao, data, hora_evento, local_evento, categoria, organizador, 
            contato_evento, inscricao, custo, rua_evento, bairro_evento, cidade_evento, estado_evento, cep_evento, email_evento, id_evento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (dados_evento['titulo'], dados_evento['descricao'], dados_evento['data_evento'], dados_evento['hora_evento'], dados_evento['local_evento'], dados_evento['categoria'], dados_evento['organizador'], 
              dados_evento['contato_evento'], dados_evento['inscricao'], dados_evento['custo'], dados_evento['rua_evento'], dados_evento['bairro_evento'], 
              dados_evento['cidade_evento'], dados_evento['estado_evento'], dados_evento['cep_evento'], dados_evento['email_evento'], dados_evento['id_evento']))
        self.conn.commit()

        # Função para processar o cadastro
    def processar_cadastro_eventos(self):
        # Obtém os dados do cadastro
        dados_evento = cadastro_eventos()

        # Conecta ao banco de dados
        self.conectar('cadastro_eventos.db')

        # Cria a tabela se ainda não existir
        self.criar_tabela()

        # Insere os dados na tabela
        self.inserir_dados(dados_evento)

        # Desconecta do banco de dados
        self.desconectar()

# Instanciando a classe BancoDeDados e chamando o método processar_cadastro
bd = BancoDeDadosEventos()
bd.processar_cadastro_eventos()