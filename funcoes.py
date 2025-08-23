def verificar_placa_nos_dados(placa, dados):
    for chave in dados:
        if placa == chave["placa"]:
            return True
        else:
            return False



def apagar_manutencoes():
    pass
