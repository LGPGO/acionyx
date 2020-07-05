from models import Arquivos, Audios, Categorias, Embarcacoes, Tutoriais

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

def insereCategoria(nome='categoriaaa'):
  categoria = Categorias(nome=nome)
  categoria.save()

def consultaCategoria():
  return Categorias.query.all()

def insereAudio(nome='audioooo', url='http://teste.com.br'):
  audio = Audios(nome=nome)
  audio.save()

def consultaAudio():
  return Audios.query.all()

def insereTutorial(nome='tutorialll', descricao='sei lá ...', status=0, id_embarcacao=1, 
id_audio=1, id_arquivo=1, tipo_arquivo='png', id_categoria=1):

  tutorial = Tutoriais(nome=nome, descricao=descricao, status=status, id_embarcacao=1,
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
  return Tutoriais.query.filter_by(id_embarcacao=id)

if __name__ == "__main__":
#   insereEmbarcacao(nome='barquinhoooo')
#   insereArquivo(nome='arquivo de testeeeee', url='http://testeeeee.com.br')
#   insereAudio(nome='Arquivoo de audioo2', url='http://urldearquivopdeaudio.com.br')
#   insereCategoria(nome='alguma categoria...')
#   insereTutorial(nome='tutorialll2', descricao='sei lá alguma coisa...', status=0, id_embarcacao=1, 
# id_audio=1, id_arquivo=1, tipo_arquivo='png', id_categoria=1)


  # consultaEmbarcacao()
  # consultaArquivo()
  # consultaAudio()
  # consultaCategoria()
  # consultaTutorial()
  pass
