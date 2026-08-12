import models
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/buscar", methods=['POST'])
def verificar_placa():
    cadastrar = request.args.get('cadastrar')
    placa_url = request.args.get('placa', '').strip().upper()
    if request.method == 'POST':
        placa_recebida = request.form.get('placa', '').upper().strip()
        veiculo, manutencoes = models.verificar_placa(placa_recebida)

        if veiculo:
            return render_template("manutencoes.html", veiculo=veiculo, manutencoes=manutencoes )
        else:
            flash(f'A placa "{placa_recebida}" não foi encontrada no sistema.', 'warning')
            return render_template('home.html', placa_nao_encontrada=placa_recebida)
    # Se o usuário clicou no link "Sim, cadastrar"
    exibir_form = True if cadastrar == 'sim' else False
    return render_template('home.html', placa_buscada=placa_url, exibir_formulario=exibir_form)
    
def executar_controller():
    models.inicializar_arquivo()
if __name__ == "__main__":
    executar_controller()
    app.run(debug=True)