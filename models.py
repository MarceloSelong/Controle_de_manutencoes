import os, sqlite3
def inicializar_arquivo():
    os.makedirs("database", exist_ok=True)  #Cria a pasta "database" se ela não existir. Se existir, ignora.
    with sqlite3.connect("database/banco.db") as conexao: #Conecta
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS veiculos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                modelo TEXT,
                marca TEXT,
                ano INTEGER,
                placa TEXT,
                quilometragem INTEGER DEFAULT 0
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS manutencoes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_carro INTEGER,
                descricao TEXT,
                custo REAL,
                data DATE,
                quilometragem INTEGER,
                FOREIGN KEY (id_carro) REFERENCES veiculos(id)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pecas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_manutencao INTEGER,
                descricao TEXT,
                marca TEXT,
                custo REAL,
                FOREIGN KEY (id_manutencao) REFERENCES manutencoes(id)
            )
        """)
        cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table'
        """)
def verificar_placa(placa_recebida):
    with sqlite3.connect("database/banco.db") as conexao:
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, modelo, ano, quilometragem, placa
            FROM veiculos
            WHERE placa = ?
            """, (placa_recebida,))
        veiculo = cursor.fetchone()
        if veiculo is None:
            return None, []
        id_do_carro = veiculo['id']
        cursor.execute("""
        SELECT descricao, data, quilometragem, custo
        FROM manutencoes
        WHERE id_carro = ?
        """, (id_do_carro,))
        manutencoes = cursor.fetchall()
    return veiculo, manutencoes