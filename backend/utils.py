from models import Arquivos, Audios, Categorias, Embarcacoes, Tutoriais
from models import db_session

def insereEmbarcacao(nome='Teste'):
  embarcacao = Embarcacoes(nome=nome)
  embarcacao.save()

# Exception has occurred: NoForeignKeysError
# Could not determine join condition between parent/child tables on relationship Arquivos.child - there are no
#  foreign keys linking these tables via secondary table 'arquivos'.  Ensure that referencing columns are
#  associated with a ForeignKey or ForeignKeyConstraint, or specify 'primaryjoin' and 'secondaryjoin' expressions.

def consultaEmbarcacao():
  return Embarcacoes.query.all()

def insereArquivo(nome='Teste', url='http://teste.com.br'):
  arquivo = Arquivos(nome=nome, url=url)
  arquivo.save()

def consultaArquivo():
  return Arquivos.query.all()

def insereCategoria(nome='categoriaaa', status=0):
  categoria = Categorias(nome=nome, status=status)
  categoria.save()
  categoria.finaliza()

def consultaCategoria():
  return Categorias.query.all()

def insereAudio(nome='audioooo', url='http://teste.com.br'):
  audio = Audios(nome=nome)
  audio.save()

def consultaAudio():
  return Audios.query.all()

def insereTutorial(nome='tutorialll', descricao='sei lá ...', status=0, id_embarcacao=1, 
id_audio=1, id_arquivo=1, tipo_arquivo='png', id_categoria=1):

  tutorial = Tutoriais(nome=nome, descricao=descricao, status=status, id_embarcacao=id_embarcacao,
   id_audio=id_audio, id_arquivo=id_arquivo, tipo_arquivo=tipo_arquivo, id_categoria=id_categoria)
  
  tutorial.save()

# altera um tutorial pelo id
def alteraTutorial(id=1, nome='nome de alteração', descricao='algo ...', status=1, tipo_arquivo='jpeg'):
  tutorial = Tutoriais.query.filter_by(id=id).first()
  tutorial.nome = nome
  tutorial.descricao = descricao
  tutorial.status = status
  tutorial.save()

def consultaTutoriais():
  return Tutoriais.query.all()

def consultaTutorialPorIdEmbarcacao(id):
  try:
    db_session.close()  
    return Tutoriais.query.filter_by(id_embarcacao=id)
  except:
    return 'Deu Erro'
  finally:
    db_session.close()  

if __name__ == "__main__":
  insereEmbarcacao(nome='barco 1')
  insereEmbarcacao(nome='barco 2')
  insereEmbarcacao(nome='barco 3')
  insereEmbarcacao(nome='barco 4')
  insereArquivo(nome='arquivo de teste 1', url='http://urldeteste1.com.br')
  insereArquivo(nome='arquivo de teste 2', url='http://urldeteste2.com.br')
  insereAudio(nome='arquivo de áudio 1', url='http://urldearquivopdeaudio1.com.br')
  insereAudio(nome='arquivo de áudio 2', url='http://urldearquivopdeaudio2.com.br')
  insereCategoria(nome='alguma categoria 1', status=0)
  insereCategoria(nome='alguma categoria 2', status=1)
  insereTutorial(nome='tutorial 1', descricao='Alguma descrição 1...', status=0, id_embarcacao=1, id_audio=1, id_arquivo=1, tipo_arquivo='png', id_categoria=1)
  insereTutorial(nome='tutorial 2', descricao='Alguma descrição 2...', status=1, id_embarcacao=1, id_audio=1, id_arquivo=1, tipo_arquivo='png', id_categoria=1)
  insereTutorial(nome='tutorial 3', descricao='Alguma descrição 3...', status=0, id_embarcacao=1, id_audio=1, id_arquivo=1, tipo_arquivo='png', id_categoria=2)
  insereTutorial(nome='tutorial 4', descricao='Alguma descrição 4...', status=1, id_embarcacao=2, id_audio=2, id_arquivo=2, tipo_arquivo='jpeg', id_categoria=2)
  insereTutorial(nome='tutorial 5', descricao='Alguma descrição 4...', status=1, id_embarcacao=3, id_audio=2, id_arquivo=2, tipo_arquivo='jpeg', id_categoria=2)
  insereTutorial(nome='tutorial 6', descricao='Alguma descrição 6...', status=1, id_embarcacao=2, id_audio=3, id_arquivo=2, tipo_arquivo='jpeg', id_categoria=2)
  insereTutorial(nome='tutorial 7', descricao='Alguma descrição 7..', status=0, id_embarcacao=3, id_audio=2, id_arquivo=2, tipo_arquivo='jpeg', id_categoria=2)

  # for i in consultaEmbarcacao():
  #   print(i.nome, i.id)
  # consultaEmbarcacao()
  # consultaArquivo()
  # consultaAudio()
  # consultaCategoria()
  # for i in consultaTutoriais():
  #   print(i.nome,i.embarcacao.id)
  pass
