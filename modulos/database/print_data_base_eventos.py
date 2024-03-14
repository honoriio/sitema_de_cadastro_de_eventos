import os
import sqlite3

class PrintBancoDeDadosEventos:
    @staticmethod
    def printar_dados_eventos(nome_banco):
        if os.path.exists(nome_banco):
            # Conectar ao banco de dados
            conn = sqlite3.connect(nome_banco)
            consulta = conn.cursor()

            # Execulta uma consulta para selecionar todos os dados da tabela 'pessoas'
            consulta.execute("SELECT * FROM eventos")

            # Recuperar os dados
            dados = consulta.fetchall()

            # Imprimir dados
            for linha in dados:
                print(linha)

            # Fechar a conexão com o banco de dados 
            conn.close()
        else:
            print('Nenhum cadastro de eventos encontrado.')

# Criando uma instância da classe e chamando o método
pb = PrintBancoDeDadosEventos()
pb.printar_dados_eventos('cadastro_eventos.db')