import sqlite3

def evento_inscricao():
    # Conectar ao banco de dados
    conn = sqlite3.connect('cadastro_eventos.db')
    cursor = conn.cursor()

    # Consulta para selecionar eventos que exigem inscrição
    consulta = "SELECT * FROM eventos WHERE inscricao = 'sim'"

    # Executar a consulta
    cursor.execute(consulta)

    # Obter os resultados
    resultados = cursor.fetchall()

    # Mostrar os resultados
    for evento in resultados:
        print(evento)

    # Fechar a conexão
    conn.close()


evento_inscricao()