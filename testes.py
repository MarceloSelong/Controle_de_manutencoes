import sqlite3
with sqlite3.connect("database/banco.db") as conexao:
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO veiculos(placa)
        VALUES('LXZ6038')
    """)