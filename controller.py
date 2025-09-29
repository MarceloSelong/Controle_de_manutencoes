import arquivos, view, validacoes, models
def nova_manutencao(id_veiculo):
    continuar_informando_servicos = "S"
    while continuar_informando_servicos == "S": #Laço pra informar os serviços
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
        descricao, custo_str = view.entrada_do_servico()                             #DESCRIÇÃO DO SERVIÇO
        while True: #Valida se é um valor numérico.                               #CUSTO DO SERVIÇO
            validacao, custo_float = validacoes.validar_custo(custo_str)
            if validacao:
                break
            else:
                custo = view.reentrada_custo()

        id_servico = arquivos.salvar_servico(id_veiculo, descricao, custo_float, data, km) #Salva o serviço realizado no BD e retorna o ID dele
        if id_servico == 0: #Se o retorno do ID da manutenção for 0, ocorreu um erro no salvamento. Então, pula o resto do laço.
            print("Informe novamente a manutenção.")
            continue
        else:
            continuar_informando_pecas = "S"
            while continuar_informando_pecas == "S": #Laço para informar as peças.
                descricao_da_peca, marca_da_peca, valor_da_peca_str = view.entrada_pecas()   #DESCRIÇÃO DA PEÇA
                while True: #Validação do valor da peça   #VALOR DA PEÇA
                    validacao, valor_da_peca_float = validacoes.validar_valor_da_peca(valor_da_peca_str)
                    if validacao:
                        break
                    else:
                        valor_da_peca_str = view.reentrada_valor_da_peca()
                retorno = arquivos.salvar_peca(id_servico, descricao_da_peca, marca_da_peca, valor_da_peca_float)
                if retorno == 0:
                    print("Repita a operação.")
                    continue
                else:
                    print(retorno)
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
            
            dados = arquivos.carregar_placas()
            
            if validacoes.verificar_placa_nos_dados(placa, dados): #Se a placa já existir no sistema, cadastraremos uma nova manutenção nele.
                id_veiculo = arquivos.retorno_id_veiculo(placa)
                nova_manutencao(id_veiculo)
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
                    while True: #Valida o ano do veículo e salva os dados no arquivo. 
                        validacao, ano = validacoes.validar_ano(ano)
                        if validacao:
                            id_veiculo = arquivos.salvar_veiculo(placa, modelo, marca, ano) #Puxa a placa do início, onde foi informada pra verificação no sistema
                            if id_veiculo == 0:
                                break
                            else:
                                break
                        else:
                            ano = view.reescolha_ano()
                    if id_veiculo == 0: #Se ocorrer erro no salvamento do veículo no arquivo, pula a iteração e retorna pro início do laço novamente.
                        continue

                    #---------------CADASTRO DA NOVA MANUTENÇÃO--------------# 
                    nova_manutencao(id_veiculo) 
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
            dados = arquivos.carregar_dados(placa)
            if not dados:
                print("\nNão existem manutenções no veículo com esta placa.\n")
            else:
                view.listar_manutencoes(dados, arquivos.tamanho_str_descricao())

        elif escolha == 3:#DELETA A MANUTENÇÃO ESCOLHIDA DO VEÍCULO
            placa = view.pedir_placa()
            while True: #Faz a validação da placa
                validacao, placa = validacoes.validar_placa(placa)
                if validacao:
                    break
                else:
                    placa = view.reescolha_da_placa()
            dados = arquivos.carregar_dados(placa)
            
            view.listar_manutencoes(dados, arquivos.tamanho_str_descricao())
            if dados != []:
                escolha = view.escolha_deletar_manutencao()
                while True:
                    validacao, escolha = validacoes.validar_escolha_de_deletar_manutencao(escolha, dados)
                    if validacao:
                        arquivos.deletar_manutencao(escolha)
                        break
                    else:
                        escolha = view.reescolha_deletar_manutencao()
                
        elif escolha == 0:
            quit()
executar_controller()