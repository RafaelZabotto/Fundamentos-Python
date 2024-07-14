import sqlite3

with sqlite3.connect('artistas.db') as conexao:
    # Criar uma conexao com o banco de dados
    sql = conexao.cursor()
    # Rodar Comando SQL
    sql.execute('create table banda(nome text, estilo text, membros integer)')

