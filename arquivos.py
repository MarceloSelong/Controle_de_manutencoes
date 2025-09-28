import os, sqlite3
def inicializar_arquivo():
    os.makedirs("database", exist_ok=True)
    if not os.path.exists("database/banco.db"):
        with sqlite3.connect("database/banco.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS veiculos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    modelo TEXT,
                    marca TEXT,
                    ano INTEGER,
                    placa TEXT
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
def carregar_placas():
    with sqlite3.connect("database/banco.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT placa
            FROM veiculos
        """)
        resultado = cursor.fetchall()
        return resultado
def salvar_veiculo(placa, modelo, marca, ano):
    #Salva os dados do veículo no BD e retorna o Id dele
    try:
        with sqlite3.connect("database/banco.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO veiculos(placa, modelo, marca, ano)
                VALUES(?, ?, ?, ?)
            """, (placa, modelo, marca, ano))
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao salvar no banco: \033[1;31m{e}\033[0m")
        return 0   
def salvar_servico(id_carro, descricao, custo, data, quilometragem):
    #Salva o serviço realizado no BD e retorna o Id dele
    try:
        with sqlite3.connect("database/banco.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO manutencoes(id_carro, descricao, custo, data, quilometragem)
                VALUES(?, ?, ?, ?, ?)
            """,(id_carro, descricao, custo, data, quilometragem))
            return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao salvar no banco: \033[1;31m{e}\033[0m")
        return 0
def salvar_peca(id_servico, descricao_da_peca, marca_da_peca, valor_da_peca):
    #Salva os dados do item utilizado no BD
    try:
        with sqlite3.connect("database/banco.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO pecas(id_manutencao, descricao, marca, custo)
                VALUES(?, ?, ?, ?)
            """, (id_servico, descricao_da_peca, marca_da_peca, valor_da_peca))
        return "Item salvo com sucesso."
    except Exception as e:
        print(f"Erro ao salvar no banco: \033[1;31m{e}\033[0m")
        return 0
def retorno_id_veiculo(placa):
    with sqlite3.connect("database/banco.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id
            FROM veiculos
            WHERE placa = ?
        """, (placa,))
        resultado = cursor.fetchone()
        return resultado[0]
def carregar_dados(placa):
    with sqlite3.connect("database/banco.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT descricao, custo, data, quilometragem
            FROM manutencoes
            JOIN veiculos ON manutencoes.id_carro = veiculos.id
            WHERE placa = ?
        """, (placa,))
        return cursor.fetchall()
def deletar_manutencao(id_manutencao):
    try:
        with sqlite3.connect("database/banco.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                DELETE FROM manutencoes
                WHERE id = ?
            """,(id_manutencao,))
            cursor.execute("""
                DELETE FROM pecas
                WHERE id_manutencao = ?
            """,(id_manutencao,))
        print("\nDeletada com sucesso.\n")
    except Exception as e:
        print(f"Erro ao apagar do banco: \033[1;31m{e}\033[0m")