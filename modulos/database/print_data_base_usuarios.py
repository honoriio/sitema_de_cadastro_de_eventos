import os
import sqlite3

from modulos.interface.elemento import linha_dupla, linha_tres

class PrintBancoDeDadosUsuarios:
    @staticmethod
    def printar_dados_usuarios(nome_banco):
        if os.path.exists(nome_banco):
            # Conectar ao banco de dados
            conn = sqlite3.connect(nome_banco)
            consulta = conn.cursor()

            # Executar uma consulta para selecionar todos os dados da tabela 'pessoas'
            consulta.execute("SELECT * FROM pessoas")

            # Recuperar os dados
            dados = consulta.fetchall()

            # Imprimir dados
            for linha in dados:
                print("{}, ID usuário: {}, Nome: {}, Data de Nascimento: {}, Celular: {}, E-mail: {}, Sexo: {}, CEP: {}".format(
                    linha[0], linha[10], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]
                ))
                linha_tres()

            # Fechar a conexão com o banco de dados 
            conn.close()
        else:
            print('Nenhum cadastro de usuário encontrado.')

# Criando uma instância da classe e chamando o método
pb = PrintBancoDeDadosUsuarios()
pb.printar_dados_usuarios('cadastro.db')

