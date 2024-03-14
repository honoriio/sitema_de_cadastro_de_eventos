# Local destinado para as importações necessarias para criação do programa
import sqlite3
from modulos.api.api import consulta_cep
from modulos.funcoes import cadastro
from modulos.api.api import imprimir_informacoes_cep

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
                celular TEXT,
                email TEXT,
                sexo TEXT,
                cep TEXT,
                localidade TEXT,
                uf TEXT,
                complemento TEXT,
                id_usuario TEXT
            )
        ''')
        self.conn.commit()

    # Função para inserir os dados do dicionário na tabela
    def inserir_dados(self, dados):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO pessoas (nome, data_nascimento, celular, email, sexo, cep, localidade, uf, complemento, id_usuario)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (dados['nome'], dados['data_nascimento'], dados['celular'], dados['email'], dados['sexo'], dados['cep'], dados['localidade'], dados['uf'], dados['complemento'], dados['id_usuario']))
        self.conn.commit()

    # Função para processar o cadastro
    def processar_cadastro(self):
        # Obtém os dados do cadastro
        dados = cadastro()

        cep = dados['cep']

        # Consulta o CEP
        cep_info = consulta_cep(cep)

        if cep_info:
            dados = {**dados, **cep_info}  # Mescla os dados do CEP com os dados do cadastro

            # Conecta ao banco de dados
            self.conectar('cadastro.db')

            # Cria a tabela se ainda não existir
            self.criar_tabela()

            # Insere os dados na tabela
            self.inserir_dados(dados)

            # Desconecta do banco de dados
            self.desconectar()

            # Imprime os dados obtidos com o cep
            #imprimir_informacoes_cep(cep)
        else:
            print("CEP não encontrado.")

# Instanciando a classe BancoDeDados e chamando o método processar_cadastro
bd = BancoDeDados()
bd.processar_cadastro()



# Campos de mudanças 

# Verificar o por que não esta sendo adicionado os dados corretamente ao banco de dados do cadastro de usuarios.

# Preciso adicionar novos parametros para que sejam adicionados os ids para cada usuario e que possa ser pesquisado cada usuario pelo seu ID..

# Mostrar as alterações feitas pelos ID de cada usuario. Exemplo, se um usuario fizer uma alterção em um evento tera um log mostrando as alterações que foram feitas por esse usuario e mostrara o seu ID..

# Fazer um teste parrudo apos adicionar as funcionalidades no programa para verificar se tudo esta funcionando perfeitamente. 

