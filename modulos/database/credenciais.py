import os 
import sqlite3

from modulos.interface.elemento import linha_tres


class CredenciaisUsuario:  
    @staticmethod  
    def credenciais(nome_banco, email, senha):
        if os.path.exists(nome_banco):
            # Conectar ao banco de dados
            conn = sqlite3.connect(nome_banco)
            consulta = conn.cursor()

            # Executar uma consulta para selecionar os dados do usuário com o email fornecido
            consulta.execute("SELECT * FROM pessoas WHERE email=?", (email,))
            usuario = consulta.fetchone()

            if usuario:  # Verifica se o usuário com o email fornecido foi encontrado
                # Recupera a senha armazenada no banco de dados
                senha_armazenada = usuario[5]  # Supondo que a coluna onde a senha está armazenada seja a quinta (índice 4)

                # Verifica se a senha fornecida corresponde à senha armazenada no banco de dados
                if senha == senha_armazenada:
                    print("Login bem-sucedido!")
                    # Você pode retornar os dados do usuário aqui se desejar
                else:
                    print("Senha incorreta.")
            else:
                print("Usuário não encontrado.")

            # Fechar a conexão com o banco de dados 
            conn.close()
        else:
            print('Nenhum cadastro de usuário encontrado.')


