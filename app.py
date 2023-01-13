from flask import Flask, render_template, request
import csv


app = Flask(__name__, template_folder='template')
registros = []
lista = []
#rotas para abrir as paginas web.

#rota principal página web.
@app.route('/', methods = ['GET'])
def principal():
    return render_template('pynet.html')

#rota home, informações sobre nosso grupo, e links para cadastros existentes e link para formulario.
@app.route('/home', methods = ['GET'])
def home():
    return render_template('home.html')

#rota para preencher o formulário.
@app.route('/formulario', methods = ['GET'])
def formulario():
    return render_template('formulario.html')

#rota se o formulário for preenchido, o usuário será redirecionado para o aviso de cadastro recebido e em seguida o arquivo csv é criado.
@app.route('/formulario', methods = ['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        registros.append(request.form.get('Nome completo'))
        registros.append(request.form.get('CPF'))
        registros.append(request.form.get('Data de Nascimento'))
        registros.append(request.form.get('Telefone de contato'))
        registros.append(request.form.get('Email'))
        registros.append(request.form.get('Cidade'))
        registros.append(request.form.get('UF'))
        print(registros)
        with open('cadastro.csv', 'a', newline='\n') as insere_linha:
            arquivo = csv.writer(insere_linha)
            arquivo.writerow(registros)
            insere_linha.close()
        registros.clear()
    return render_template('cadastro.html')

app.run(debug = True)