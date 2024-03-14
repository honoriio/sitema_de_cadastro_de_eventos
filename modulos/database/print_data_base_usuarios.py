import os
import sqlite3

class PrintBancoDeDadosUsuarios:
    @staticmethod
    def printar_dados_usuarios(nome_banco):
        if os.path.exists(nome_banco):
            # Conectar ao banco de dados
            conn = sqlite3.connect(nome_banco)
            consulta = conn.cursor()

            # Execulta uma consulta para selecionar todos os dados da tabela 'pessoas'
            consulta.execute("SELECT * FROM pessoas")

            # Recuperar os dados
            dados = consulta.fetchall()

            # Imprimir dados
            for linha in dados:
                print(linha)

            # Fechar a conexão com o banco de dados 
            conn.close()
        else:
            print('Nenhum cadastro de usúario encontrado.')

# Criando uma instância da classe e chamando o método
pb = PrintBancoDeDadosUsuarios()
pb.printar_dados_usuarios('cadastro.db')
