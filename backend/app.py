import os, sys
from flask import Flask, redirect, render_template, render_template_string, send_from_directory
from models import Arquivos, Audios, Categorias, Tutoriais, Embarcacoes, db_session
from flask_restful import Resource, Api, request
from utils import *

pastaRaiz       = os.path.realpath(__file__ + '/../..') # caminho do diretório até o projeto acionyx
pastaTemplates  = os.path.join(pastaRaiz,'frontend')
pastaCSS        = os.path.join(pastaTemplates, 'css')
pastaIMG        = os.path.join(pastaTemplates, 'img')

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
        dados = request.form
        
        tutorial = insereTutorial(nome=dados['nome'], descricao=dados['descricao'],
        id_embarcacao=dados['id_embarcacao'], id_categoria=dados['id_categoria'])
        tutorial.save()
        return redirect('/success')


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

@app.route('/embarcacao/<int:id>/add-activity', methods = ['GET'])
def addactivity(id):
    embarcacao = Embarcacoes.query.filter_by(id=id).first()

    if embarcacao:
        categorias = Categorias.query.all()

        return render_template('add-activity.html', categorias=categorias,
        embarcacao=embarcacao)

@app.route('/success', methods = ['GET'])
def sucesso():
    # funcaoInicial()
    return render_template('success.html')

@app.route('/embarcacao/<int:id>/audios', methods = ['GET'])
def audio(id):
    embarcacao = Embarcacoes.query.filter_by(id=id).first()
    # funcaoInicial()
    if embarcacao:
        atividades = consultaTutorialPorIdEmbarcacao(id)
    return render_template('audios.html', atividades=atividades, embarcacao=embarcacao)


@app.route('/embarcacao/<int:id>', methods = ['GET'])
def show_embarcacao(id):
    atividades = consultaTutorialPorIdEmbarcacao(id)

    return render_template('embarcacao.html', atividades=atividades)

@app.route('/embarcacao/<int:id>/atividade/<int:id2>', methods = ['GET'])
def show_atividade(id, id2):
    atividade = Tutoriais.query.filter_by(id=id2).first()

    return render_template('atividade.html', atividade=atividade)

# @app.route('/padrao', methods = ['GET'])
# def padrao():
#     return render_template('padrao.html')

@app.route('/teste', methods = ['GET'])
def teste():
    return render_template('teste.html')

# @app.route('/delete/<int:idEmbarcacao>', methods= ['GET'])
# def delete(idEmbarcacao):
#     print(pastaCSS)
#     print(pastaIMG)
#     return render_template('delete.html', id=idEmbarcacao)

# @app.route('/delete_sucess', methods= ['GET'])
# def deleteOk():
#     return render_template('delete_success.html')


# def qualquerRota(caminho):
#     return render_template(caminho+'.html')

@app.errorhandler(404)
def paginaNaoEncontrada(error):
    return render_template('página não encontrada.html'), 404

api.add_resource(Embarcacao, '/embarcacoes')    
api.add_resource(Tutorial, '/tutoriais')
# app.add_url_rule('/<path:caminho>', view_func=qualquerRota)

if __name__ == "__main__":
    app.run(debug=True)
