import models
from flask import Flask, flash, render_template, request
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/manutencoes", methods=['POST'])
def listar_manutencoes():
    placa = request.form.get('placa', '').upper().strip()
    veiculo, manutencoes = models.verificar_banco(placa) #Se a placa existir no BD, retorna os dados do veículo e suas manutenções. Se não, retorna None e uma lista vazia.
    if veiculo:
        return render_template('manutencoes.html', veiculo=veiculo, manutencoes=manutencoes, veiculo_encontrado=True)
    else:
        #Se o veículo não foi encontrado no BD, envia um flag que renderiza um Warning que dá opção de incluir um novo veículo no registro ou não.
        return render_template('home.html', placa=placa, veiculo_encontrado=False)

@app.route("/manutencoes/adicionar", methods=['POST'])
def funcao():
    dados = request.form.to_dict()
    salvo, string = models.salvar_manutencao(dados)
    if salvo:
        placa = request.form.get('placa', '').upper().strip()
        veiculo, manutencoes = models.verificar_banco(placa) #Retorna os dados do veículo e suas manutenções. Se não, retorna None e uma lista vazia.
        return render_template('manutencoes.html', veiculo=veiculo, manutencoes=manutencoes, veiculo_encontrado=True)
    else:
        print(string)

@app.route('/manutencao/<int:id>/excluir', methods=['POST'])    
def exluir_manutencao(id):
    placa = request.form.get('placa')
    state = models.excluir_manutencao(id)
    if state:
        flash('Manutenção excluída com sucesso!', 'success')
        veiculo, manutencoes = models.verificar_banco(placa)
        return render_template('manutencoes.html', veiculo=veiculo, manutencoes=manutencoes, veiculo_encontrado=True)
    else:
        flash(f'Erro ao excluir manutenção: {state}', 'danger')
        veiculo, manutencoes = models.verificar_banco(placa)
        return render_template('manutencoes.html', veiculo=veiculo, manutencoes=manutencoes, veiculo_encontrado=True)
@app.route("/cadastrar_veiculo", methods=['POST'])
def cadastrar_veiculo():
    placa = request.form.get('placa', '').upper().strip()
    return render_template('cadastrar_veiculo.html', placa=placa)

@app.route("/salvar_veiculo", methods=["POST"])
def salvar_veiculo():
    dados_do_veiculo = request.form.to_dict()
    validacao, resposta = models.salvar_veiculo(dados_do_veiculo)
    veiculo, manutencoes = models.verificar_banco(dados_do_veiculo['placa'])
    return render_template('manutencoes.html', validacao=validacao, string=resposta, veiculo=veiculo, manutencoes=manutencoes)


def executar_controller():
    models.inicializar_arquivo()
if __name__ == "__main__":
    executar_controller()
    app.run(debug=True)


#TODO Deve ser adicionado a função de editar registros em manutencoes.html
#TODO Deve ser adicionado função que lista veiculos existentes
#TODO Deve ser adicionado a função de excluir veículos do registro
