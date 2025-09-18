import os, json, sqlite3
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

def carregar_dados():
    with open("manutencoes.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo) 
    return dados

def carregar_placas():
    with sqlite3.connect("database/banco.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT placa
            FROM veiculos
        """)
        resultado = cursor.fetchall()
        return resultado

def salvar_dados(dados):
    with open("manutencoes.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    return "Dados salvos com sucesso."