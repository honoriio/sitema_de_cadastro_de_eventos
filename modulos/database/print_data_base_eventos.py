import os
import sqlite3

class PrintBancoDeDadosEventos:
    @staticmethod
    def printar_dados_eventos(nome_banco):
        if os.path.exists(nome_banco):
            # Conectar ao banco de dados
            conn = sqlite3.connect(nome_banco)
            consulta = conn.cursor()

            # Execulta uma consulta para selecionar todos os dados da tabela 'eventos'
            consulta.execute("SELECT * FROM eventos")

            # Recuperar os dados
            dados = consulta.fetchall()

            # Imprimir dados
            for linha in dados:
                print("""
                       ID do Evento:..........{}
                       Título:................{}
                       Descrição:.............{}
                       Data:..................{}
                       Hora do Evento:........{}
                       Local do Evento:.......{}
                       Categoria:.............{}
                       Organizador:...........{}
                       Contato:...............{}
                       Inscrição:.............{}
                       Custo:.................{}
                       Rua:...................{}
                       Bairro:................{}
                       Cidade:................{}
                       Estado:................{}
                       CEP:...................{}
                       E-mail:................{}
                      """.format(
                    linha[17], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16]))

            # Fechar a conexão com o banco de dados 
            conn.close()
        else:
            print('Nenhum cadastro de eventos encontrado.')

# Criando uma instância da classe e chamando o método
pb = PrintBancoDeDadosEventos()
pb.printar_dados_eventos('cadastro_eventos.db')






