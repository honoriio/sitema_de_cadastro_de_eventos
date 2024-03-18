import os 
import sqlite3
import time

from modulos.bibliotecas.uuid import limpar_tela
from modulos.interface.elemento import linha, linha_tres

class CredenciaisUsuario:  
    @staticmethod  
    def credenciais(nome_banco, email, senha):
        senha_armazenada = None  # Valor padrão para senha_armazenada
        if os.path.exists(nome_banco):
            conn = sqlite3.connect(nome_banco)
            consulta = conn.cursor()

            consulta.execute("SELECT * FROM pessoas WHERE email=?", (email,))
            usuario = consulta.fetchone()

            if usuario:  
                senha_armazenada = usuario[5]  # Armazena a senha encontrada no banco de dados

                if senha == senha_armazenada:
                    print("Login bem-sucedido!")
                    # Você pode retornar os dados do usuário aqui se desejar
                else:
                    linha()
                    print("Senha incorreta.")
                    linha()
                    time.sleep(2)
                    limpar_tela()
            else:
                linha()
                print("Usuário não encontrado.")
                linha()
                time.sleep(2)
                limpar_tela()

            conn.close()
        else:
            linha()
            print('Nenhum cadastro de usuário encontrado.')
            linha()
            time.sleep(2)
            limpar_tela()
        
        return senha_armazenada  # Retorna senha_armazenada





