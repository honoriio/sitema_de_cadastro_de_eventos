import sqlite3


class PrintBancoDeDadosEventos():
    @staticmethod
    def printar_dados_eventos():
        # Conectar ao banco de dados
        conn = sqlite3.connect('cadastro_eventos.db')
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

pb = PrintBancoDeDadosEventos()
pb.printar_dados_eventos()