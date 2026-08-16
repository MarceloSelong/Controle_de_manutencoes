import models
from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/buscar", methods=['POST'])
def verificar_placa():
    placa_recebida = request.form.get('placa', '').upper().strip()
    veiculo, manutencoes = models.verificar_placa(placa_recebida) #Se a placa existir no BD, retorna os dados do veículo e suas manutenções. Se não, retorna None e uma lista vazia.
    if veiculo:
        return render_template('manutencoes.html', veiculo=veiculo, manutencoes=manutencoes)
    else:
        #Se o veículo não foi encontrado no BD, envia um flag que renderiza um Warning que dá opção de incluir um novo veículo no registro ou não.
        return render_template('home.html', placa=placa_recebida, veiculo_nao_encontrado=True)





def executar_controller():
    models.inicializar_arquivo()
if __name__ == "__main__":
    executar_controller()
    app.run(debug=True)