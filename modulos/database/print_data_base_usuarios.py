import sqlite3


class PrintBancoDeDadosUsuarios():
    @staticmethod
    def printar_dados_usuarios():
        # Conectar ao banco de dados
        conn = sqlite3.connect('cadastro.db')
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

pb = PrintBancoDeDadosUsuarios()
pb.printar_dados_usuarios()