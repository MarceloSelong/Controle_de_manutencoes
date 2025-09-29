import sqlite3
with sqlite3.connect("database/banco.db") as conexao:
    cursor = conexao.cursor()
    cursor.execute("""
        DELETE FROM manutencoes
    """)
    cursor.execute("""
        DELETE FROM sqlite_sequence WHERE name='manutencoes'
    """)