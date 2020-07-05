import os
from flask import Flask, redirect, render_template, render_template_string, send_from_directory
from models import Arquivos, Audios, Categorias, Tutoriais, Embarcacoes, db_session
from flask_restful import Resource, Api, request
from utils import *

pastaRaiz = os.path.abspath('')
pastaTemplates = os.path.join(pastaRaiz,'frontend')
pastaCSS = os.path.join(pastaTemplates, 'css')
pastaIMG = os.path.join(pastaTemplates, 'img')

app = Flask(__name__, 
# static_url_path=pastaStaticTemplates ,
template_folder=pastaTemplates

)

def funcaoInicial():
    # app.send_static_file()
    pass


api = Api(app)

class Tutorial(Resource):
    def get(self):
        tutoriais = Tutoriais.query.all()

        return [
            {'id': tutorial.id, 
            'nome': tutorial.nome,
            'descrição': tutorial.descricao,
            'Nome da Embarcação': tutorial.embarcacao.nome,
            'Nome do Áudio' : tutorial.audio.nome,
            'Nome da Categoria': tutorial.categoria.nome,
            'Nome do Arquivo': tutorial.arquivo.nome
            }  for tutorial in tutoriais
        ]

    def post(self):
        dados = request.json

        tutorial = Tutoriais(nome=dados['nome'], descricao=dados['descricao'],
        status=dados['status'], id_embarcacao=dados['id_embarcacao'], id_audio=dados['id_audio'],
        id_arquivo=dados['id_arquivo'], id_categoria=dados['id_categoria'], tipo_arquivo=dados['tipo_arquivo'])
        tutorial.save()

        return {
            'nome': tutorial.nome,
            'descricao': tutorial.descricao
        }

    def put(self):
        dados = request.json
        tutorial = Tutoriais.query.filter_by(id=dados['id']).first()
        tutorial.nome = dados['nome'] if ('nome' in dados) else dados['nome']
        tutorial.descricao = dados['descricao'] if ('descricao' in dados) else dados['descricao']
        tutorial.status = dados['status'] if ('status' in dados) else dados['status']
        tutorial.save() 
        return {'id':tutorial.id,'nome':tutorial.nome,'descricao':tutorial.descricao,'status':tutorial.status}

    def delete(self):
        dados = request.json
        tutorial = Tutoriais.query.filter_by(id=dados['id']).first()
        tutorial.delete()

        return {
            'status': 'sucesso',
            'mensagem': 'O Tutorial de ID {} foi deletado!'.format(tutorial.id)
        }
        pass
    pass

class Embarcacao(Resource):
    def get(self):
        embarcacoes = Embarcacoes.query.all()

        return [
            {'id': embarcacao.id, 
            'nome': embarcacao.nome
            }  for embarcacao in embarcacoes
        ]

    def post(self):
        dados = request.form

        embarcacao = Embarcacoes(nome=dados['nome'])
        embarcacao.save()

        return redirect("/success")

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(pastaCSS, path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(pastaIMG, path)

@app.route('/', methods = ['GET'])
def index():
    # app.send_static_file()
    funcaoInicial()

    lista = consultaEmbarcacao()
    
    return render_template('index.html', lista=lista)

@app.route('/add-ship', methods = ['GET'])
def addship():
    # funcaoInicial()
    return render_template('add-ship.html')

@app.route('/add-activity', methods = ['GET'])
def addactivity():
    # funcaoInicial()
    return render_template('add-activity.html')

@app.route('/success', methods = ['GET'])
def sucesso():
    # funcaoInicial()
    return render_template('success.html')

@app.route('/embarcacao/<int:id>', methods = ['GET'])
def show_embarcacao(id):
    atividades = consultaTutorialPorIdEmbarcacao(id)

    return render_template('embarcacao.html', atividades=atividades)


# @app.route('/<path:path>', methods = ['GET'])
# def qualquerCaminho(path):  
#     # embarcacoes = Embarcacoes.query.all()
#     # print(embarcacoes)
#     # funcaoInicial()
#     print(path)
#     return render_template(path+'.html', 
#     # testes = embarcacoes
#     )     
#     # embarcacoes=Embarcacao()
    

api.add_resource(Embarcacao, '/embarcacoes')    
api.add_resource(Tutorial, '/tutoriais')

if __name__ == "__main__":
    app.run(debug=True)
    # print(os.path.abspath(os.path.dirname(__file__)))
