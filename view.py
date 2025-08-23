def menu():
    print("Informe o que deseja fazer com as suas manutenções:")
    escolha = input("""[1] criar nova manutenção
[2] listar manutenções existentes
[3] apagar manutenção
[0] sair: """).strip()
    return escolha
        
def reescolha_do_menu():
    reescolha = input("Escolha incorreta, informe 0, 1, 2 ou 3: ")
    return reescolha

def pedir_placa():
    placa = input("Informe a placa do veículo: ").strip().upper().replace("-", "").replace(" ", "")
    return placa

def reescolha_da_placa():
    placa = input("Placa informada incorretamente, digite no formato ABC1D23 ou ABC1234: ").strip().upper().replace("-", "").replace(" ", "")
    return placa

def escolha_de_cadastrar_novo_veiculo():
    escolha = input("A placa informada não existe no sistema, deseja cadastrar novo veículo ? [S/N]: ").upper().strip()
    return escolha

def reescolha_de_cadastrar_novo_veiculo():
    escolha = input("Escolha inválida, digite 'S' ou 'N': ").upper().strip()
    return escolha

def cadastro_novo_veiculo():
    modelo = input("Informe o modelo: ").strip()
    marca = input("Informe a marca: ").strip()
    ano = input("Informe o ano: ").strip()
    return modelo, marca, ano

def reescolha_ano():
    reescolha = input("Ano inválido, informe um número inteiro: ").strip()
    return reescolha

def km_data_nova_manutencao():
    data = input("Informe a data da manutenção: ").strip()
    quilometragem = input("Informe a quilometragem: ").strip()
    return quilometragem, data

def reentrada_da_quilometragem():
    reentrada = input("Quilometragem inválida, informe novamente: ").strip()
    return reentrada

def reentrada_da_data():
    reentrada = input("Data incorreta, informe corretamente no formato DD/MM/AAAA: ").strip()
    return reentrada

def entrada_do_servico():
    descricao = input("Informe o serviço que foi realizado: ").strip()
    valor_da_mao_de_obra = input("Informe o valor da mão de obra para o serviço informado: ").strip().replace(",", ".")
    return descricao, valor_da_mao_de_obra

def reentrada_custo():
    reentrada = input("Valor inválido, informe um valor numérico: ").strip()
    return reentrada

def entrada_pecas():
    descricao_da_peca = input("Informe a peça que foi utilizada: ").strip()
    valor_peca = input("Informe o valor dela: ").strip().replace(",", ".").replace(" ", "")
    return descricao_da_peca, valor_peca

def reentrada_valor_da_peca():
    reentrada = input("Valor inválido, informe um valor numérico: ").strip().replace(",", ".").replace(" ", "")
    return reentrada

def informar_mais_pecas():
    continuar = input("Deseja informar mais peças? [S/N]: ").strip().upper()
    return continuar

def reescolha_informar_mais():
    reescolha = input("Escolha inválida, aperte S ou N: ").strip().upper()
    return reescolha

def informar_mais_servicos():
    continuar = input("Deseja informar mais serviços? [S/N]: ").strip().upper()
    return continuar

def listar_manutencoes(carro):
    print(f"\nMarca: {carro['marca']}.")
    print(f"Modelo: {carro['modelo']}.")
    print(f"Ano: {carro['ano']}.\n")
    for indice, servico in enumerate(carro['lista_de_manutencoes'], start=1):
        print(f"{[indice]} Serviço: {servico['descricao']}.")      
        print("Itens utilizados:")
        for peca in servico["lista_de_pecas"]:
            print(f"{peca['descricao']}, custo: R${peca['custo']:.2f}.")
        print(f"Mão de obra: R${servico['custo']:.2f}.\n")

def escolha_deletar_manutencao():
    escolha = input("Escolha a numeração da manutenção a ser apagada conforme a lista acima: ")
    return escolha

def reescolha_deletar_manutencao():
    escolha = input("ESCOLHA INCORRETA, informe o numero conforme a lista acima: ")
    return escolha