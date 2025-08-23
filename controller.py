import arquivos, view, validacoes, funcoes, models
def nova_manutencao():
    km, data = view.km_data_nova_manutencao() #Entrada da data e km           #KM E DATA
    while True: #Validação da km
        validacao, km = validacoes.validacao_do_km(km)
        if validacao:
            break
        else: 
            km = view.reentrada_da_quilometragem()
    
    while True: #Validação da data
        validacao, data = validacoes.validacao_da_data(data) 
        if validacao:
            break
        else:
            data = view.reentrada_da_data()

    continuar_informando_servicos = "S"
    while continuar_informando_servicos == "S": #Laço pra informar os serviços
        descricao, custo = view.entrada_do_servico() #DESCRIÇÃO DO SERVIÇO
        while True: #Valida se é um valor numérico. #CUSTO DO SERVIÇO
            validacao, custo_float = validacoes.validar_custo(custo)
            if validacao:
                break
            else:
                custo = view.reentrada_custo()
        lista_de_obj_pecas = [] #LISTA DE PEÇAS OBJETO
        
        continuar_informando_pecas = "S"
        while continuar_informando_pecas == "S": #Laço para informar as peças. #LISTA DE OBJETOS DAS PEÇAS
            descricao_da_peca, valor_da_peca_str = view.entrada_pecas()   #DESCRIÇÃO DA PEÇA
            while True: #Validação do valor da peça   #VALOR DA PEÇA

                validacao, valor_da_peca_float = validacoes.validar_valor_da_peca(valor_da_peca_str)
                if validacao:
                    break
                else:
                    valor_da_peca_str = view.reentrada_valor_da_peca()

            obj_peca = models.Pecas(descricao_da_peca, valor_da_peca_float) #OBJETO PEÇA INSTANCIADO
            lista_de_obj_pecas.append(obj_peca.para_dict()) #Joga o dicionário dos objetos peca, pra dentro de uma lista. Essa lista será colocada dentro do objeto serviço logo á frente.
            continuar_informando_pecas = view.informar_mais_pecas()
            while True: #Validação da escolha de adicionar mais peças
                validacao, continuar_informando_pecas = validacoes.validar_escolha(continuar_informando_pecas)
                if validacao:
                    break
                else:
                    continuar_informando_pecas = view.reescolha_informar_mais()
        
        continuar_informando_servicos = view.informar_mais_servicos() 
        while True: #Validação da escolha de adicionar mais serviços
            validacao, continuar_informando_servicos = validacoes.validar_escolha(continuar_informando_servicos)
            if validacao:
                break
            else:
                continuar_informando_servicos = view.reescolha_informar_mais()
        
        obj_servico = models.Servico(descricao, custo_float, data, km, lista_de_obj_pecas) #OBJETO SERVIÇO INSTANCIADO
    return obj_servico.para_dict()

def executar_controller():
    arquivos.inicializar_arquivo()
    while True:
        escolha = view.menu()
    
        while True: #Faz a validação da escolha do usuário pra saber qual processo o código irá realizar
            validacao, escolha = validacoes.validar_escolha_do_menu(escolha)
            if validacao == True:
                break
            else:
                escolha = view.reescolha_do_menu()
        
        if escolha == 1: #ESCOLHA DE CRIAR NOVA MANUTENÇÃO
            placa = view.pedir_placa()
            while True: #Faz a validação da placa
                validacao, placa = validacoes.validar_placa(placa)
                if validacao:
                    break
                else:
                    placa = view.reescolha_da_placa()
            dados = arquivos.carregar_dados()
             
            if funcoes.verificar_placa_nos_dados(placa, dados): #Se a placa já existir no sistema, cadastraremos uma nova manutenção nele.
                manutencao = nova_manutencao()
                dados = arquivos.carregar_dados()
                for carro in dados:
                    if carro["placa"] == placa:
                        carro["lista_de_manutencoes"].append(manutencao)
                print(arquivos.salvar_dados(dados))

            else: #Se a placa não existir no sistema, pergunta se deseja cadastrar novo veículo.
                escolha = view.escolha_de_cadastrar_novo_veiculo()
                while True: # Valida a escolha de cadastrar novo veículo
                    validacao = validacoes.validar_escolha_de_cadastrar_novo_veiculo(escolha) 
                    if validacao:
                        break
                    else:
                        escolha = view.reescolha_de_cadastrar_novo_veiculo()
                
                if escolha == "S": #Cadastra novo veículo
                    modelo, marca, ano = view.cadastro_novo_veiculo() #Entrada de dados pro cadastrodo novo veículo.
                    while True: #Valida o ano do veículo e salva os dados validados no arquivo. 
                        validacao, ano = validacoes.validar_ano(ano)
                        if validacao:
                            veiculo = models.Veiculo(placa, modelo, marca, ano)
                            dados = arquivos.carregar_dados()
                            dados.append(veiculo.para_dict())
                            print(arquivos.salvar_dados(dados))
                            break
                        else:
                            ano = view.reescolha_ano()
                    #---------------CADASTRO DA NOVA MANUTENÇÃO--------------#
                    manutencao = nova_manutencao() #Recebe a lista de objetos da manutenção realizada
                    dados = arquivos.carregar_dados()
                    for carro in dados:
                        if carro["placa"] == placa:
                            carro["lista_de_manutencoes"].append(manutencao) #Adiciona a nova manutenção na lista de manutenções do respectivo veiculo
                    print(arquivos.salvar_dados(dados))

                else: #Retorna ao menu de escolha
                    pass
 
        elif escolha == 2: #LISTA AS MANUTENÇÕES DO VEÍCULO ESCOLHIDO
            placa = view.pedir_placa()
            while True: #Faz a validação da placa
                validacao, placa = validacoes.validar_placa(placa)
                if validacao:
                    break
                else:
                    placa = view.reescolha_da_placa()
            dados = arquivos.carregar_dados()
            if dados == []:
                print("Arquivo vazio.")
            else:
                for carro in dados:
                    if carro["placa"] == placa:
                        dados_do_veiculo = carro
                        view.listar_manutencoes(dados_do_veiculo)
                    else:
                        print(f"\nNão existe cadastro do veículo de placa {placa}.\n")
            
        elif escolha == 3:
            placa = view.pedir_placa()
            while True: #Faz a validação da placa
                validacao, placa = validacoes.validar_placa(placa)
                if validacao:
                    break
                else:
                    placa = view.reescolha_da_placa()
            dados = arquivos.carregar_dados()
            for carro in dados:
                if carro["placa"] == placa:
                    dados_do_carro = carro.copy()
                    view.listar_manutencoes(dados_do_carro)
                    escolha = view.escolha_deletar_manutencao()
                    while True: #Validação da escolha
                        validacao, escolha = validacoes.validar_escolha_de_deletar_manutencao(escolha, len(dados_do_carro["lista_de_manutencoes"]))
                        if validacao:
                            break
                        else:
                            escolha = view.reescolha_deletar_manutencao()
                    del dados_do_carro["lista_de_manutencoes"][escolha-1]
                    print(arquivos.salvar_dados(dados))
                else:
                    print(f"\nNão existem manutenções no veículo de placa {placa}.\n")

            

        
        
        
        elif escolha == 0:
            quit()

executar_controller()