import sqlite3
from modulos.database.eventos_com_inscricao import evento_inscricao



conn = sqlite3.connect('cadastro_eventos.db')
cursor = conn.cursor()

nome_indice = 'inscricao'

consulta = f"SELECT * FROM sqlite_master WHERE type='index' AND name='{nome_indice}'"

cursor.execute(consulta)

resultado = cursor.fetchall()

conn.close()

if resultado:  # Verifica se há algum resultado retornado
    # Ajuste para acessar corretamente o valor da tupla
    if resultado[0][4] == 'sim':
          
        evento_inscricao()



