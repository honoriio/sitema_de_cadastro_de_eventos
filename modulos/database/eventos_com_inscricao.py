import os
import sqlite3

from modulos.interface.elemento import linha_tres

class PrintEventosInscricao:
    @staticmethod
    def printar_eventos_inscricao(nome_banco):
        if os.path.exists(nome_banco):
            # Conectar ao banco de dados
            conn = sqlite3.connect(nome_banco)
            cursor = conn.cursor()

            # Executar uma consulta para selecionar todos os dados da tabela 'eventos'
            consulta_sql = "SELECT * FROM eventos WHERE inscricao = 'sim'"

            # Executar a consulta SQL
            cursor.execute(consulta_sql)

            # Recuperar os dados
            dados = cursor.fetchall()
            cont = 0
            # Imprimir dados
            for linha in dados:
                cont = cont + 1
                print(f'Evento de número {cont}')
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
                linha_tres()

            # Fechar a conexão com o banco de dados 
            conn.close()
        else:
            print('Nenhum cadastro de eventos encontrado.')

# Criando uma instância da classe e chamando o método
pb = PrintEventosInscricao()
pb.printar_eventos_inscricao('cadastro_eventos.db')
