import os, json
def inicializar_arquivo():
    if not os.path.exists("manutencoes.json"):
        with open("manutencoes.json", "w", encoding="utf-8") as arquivo:
            json.dump({}, arquivo, ensure_ascii=False, indent=4)

def carregar_dados():
    with open("manutencoes.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo) 
    return dados

def salvar_dados(dados):
    with open("manutencoes.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    return "Dados salvos com sucesso."