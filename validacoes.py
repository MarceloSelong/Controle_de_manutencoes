import re
from datetime import datetime
def validar_escolha_do_menu(escolha):
    try:
        escolha_int = int(escolha)
        if escolha_int in (0,1,2,3):
            return True, escolha_int
        else:
            return False, escolha

    except ValueError:
        return False, escolha

def validar_placa(placa):
    if re.fullmatch(r"^[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}$", placa) or re.fullmatch(r"^[A-Z]{3}[0-9]{4}$", placa):
        return True, placa
    else:
        return False, placa

def validar_escolha_de_cadastrar_novo_veiculo(escolha):
    if escolha in ("S", "N"):
        return True
    else:
        return False

def validar_ano(ano):
    try:
        ano_int = int(ano)
        return True, ano_int
    except ValueError:
        return False, ano
    
def validacao_do_km(km):
    try:
        km_int = int(km)
        return True, km_int
    except ValueError:
        return False, km


def validacao_da_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return True, data.strftime("%d/%m/%Y")
    except ValueError:
        return False
    
def validar_custo(custo_str):
    try:
        custo_float = float(custo_str)
        return True, custo_float
    except ValueError:
        return False, custo_str
    
def validar_valor_da_peca(valor_da_peca_str):
    try:
        valor_da_peca_float = float(valor_da_peca_str)
        return True, valor_da_peca_float
    except ValueError:
        return False, valor_da_peca_str

def validar_escolha(escolha):
    if escolha in ("S", "N"):
        return True, str(escolha)
    else:
        return False, escolha

def validar_escolha_de_deletar_manutencao(escolha, tamanho_dados_do_carro):
    try:
        escolha_int = int(escolha)
        if 0 < escolha_int <= tamanho_dados_do_carro:
            return True, escolha_int
        else:
            return False, escolha_int
    except:
        return False

def verificar_placa_nos_dados(placa, dados):
    for linha in dados:
        if linha[0] == placa:
            return True
    else:
        return False