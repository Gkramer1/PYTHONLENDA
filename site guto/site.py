# imports das ferramentas necessárias
from flask import Flask, render_template, redirect, request
from inicial import Investimento
from cartinv import Carteira_investimento


# cria a rota da pagina principal
app = Flask(__name__)
@app.route('/')
def invs():
    return render_template ('siteinv.html')

# cria uma rota para a página citada
@app.route('/paginaguto')
def gutopic():
    return render_template('/paginaguto.html')

# comando para executar o programa

@app.route('/TD')
def tdto():
    return render_template('/td.html')

@app.route('/CDB')
def cdbb():
    return render_template('/cdb.html')

@app.route('/LCILCA')
def lci():
    
    return render_template('/lcilca.html')

@app.route('/LC')
def cdb():
    return render_template('/lc.html')

@app.route('/salvar', methods=['POST'])
def salvar():
        aporte = request.form['aporte']
        rendimento_mensal = request.form['rendimento_mensal']
        rendimento_anual = request.form['rendimento_anual']
        # novo_investimento = Save(aporte, rendimento_mensal, rendimento_anual)
        # lista_investimento.append(novo_aluno)
        return redirect('/salvo')

app.run()