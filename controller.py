import models
from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/buscar", methods=['POST'])
def verificar_banco():
    placa_recebida = request.form.get('placa', '').upper().strip()
    veiculo, manutencoes = models.verificar_banco(placa_recebida) #Se a placa existir no BD, retorna os dados do veículo e suas manutenções. Se não, retorna None e uma lista vazia.
    if veiculo:
        return render_template('manutencoes.html', veiculo=veiculo, manutencoes=manutencoes)
    else:
        #Se o veículo não foi encontrado no BD, envia um flag que renderiza um Warning que dá opção de incluir um novo veículo no registro ou não.
        return render_template('home.html', placa=placa_recebida, veiculo_encontrado=False)

@app.route("/cadastrar_veiculo", methods=['POST'])
def cadastrar_veiculo():
    placa = request.form.get('placa', '').upper().strip()
    return render_template('cadastrar_veiculo.html', placa=placa)

#FIXME
@app.route("/salvar_veiculo", methods=["POST"])
def salvar_veiculo():
    dados_do_veiculo = request.form.to_dict()
    validacao, resposta = models.salvar_veiculo(dados_do_veiculo)

    placa = request.form.get('placa', '').upper().strip()
    veiculo, manutencoes = models.verificar_banco(placa)
    return render_template('manutencoes.html', validacao=validacao, string=resposta, veiculo=veiculo, manutencoes=manutencoes)



def executar_controller():
    models.inicializar_arquivo()
if __name__ == "__main__":
    executar_controller()
    app.run(debug=True)



#TODO Deve ser adicionado a função de excluir registros em manutencoes.html
#TODO Deve ser adicionado a função de inserir registros em manutencoes.html
#TODO Deve ser adicionado a função de editar registros em manutencoes.html
#TODO Deve ser adicionado função que lista veiculos existentes
#TODO Deve ser adicionado a função de excluir veículos do registro
#FIXME Deve ser refatorada a função de salvar_veiculo para que retorne pra tela de manutencoes do veículo recém cadastrado