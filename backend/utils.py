from models import Arquivos, Audios, Categorias, Embarcacoes, Tutoriais

def insereEmbarcacao(nome='Teste'):
  embarcacao = Embarcacoes(nome=nome)
  embarcacao.save()

# Exception has occurred: NoForeignKeysError
# Could not determine join condition between parent/child tables on relationship Arquivos.child - there are no
#  foreign keys linking these tables via secondary table 'arquivos'.  Ensure that referencing columns are
#  associated with a ForeignKey or ForeignKeyConstraint, or specify 'primaryjoin' and 'secondaryjoin' expressions.

def consultaEmbarcacao():
  embarcacao = Embarcacoes.query.all()
  print(embarcacao)

def insereArquivo(nome='Teste', url='http://teste.com.br'):
  arquivo = Arquivos(nome=nome, url=url)
  arquivo.save()

def consultaArquivo():
  arquivo = Arquivos.query.all()
  print(arquivo)

def insereCategoria(nome='categoriaaa'):
  categoria = Categorias(nome=nome)
  categoria.save()

def consultaCategoria():
  categoria = Categorias.query.all()
  print(categoria)

def insereAudio(nome='audioooo', url='http://teste.com.br'):
  audio = Audios(nome=nome)
  audio.save()

def consultaAudio():
  audio = Audios.query.all()
  print(audio)


# class Tutoriais(Base, Metodos):
#   __tablename__ = 'tutoriais'

#   id = Column(Integer, primary_key = True)
#   nome = Column(String(20))
#   descricao = Column(String(100))
#   status = Column(Boolean)
#   id_embarcacao = Column(Integer, ForeignKey('embarcacoes.id'))
#   id_audio = Column(Integer, ForeignKey('audios.id'))
#   id_arquivo = Column(Integer, ForeignKey('arquivos.id'))
#   tipo_arquivo = Column(String(3))
#   id_categoria = Column(Integer, ForeignKey('categorias.id'))

#   # Relacionamentos
#   arquivos = relationship("Arquivos")
#   categorias = relationship("Categorias")
#   embarcacoes = relationship("Embarcacoes")
#   audios = relationship("Audios")
def insereTutorial(nome='tutorialll', descricao='sei lá ...', status=0, id_embarcacao=1, 
id_audio=1, id_arquivo=1, tipo_arquivo='png', id_categoria=1):

  tutorial = Tutoriais(nome=nome, descricao=descricao, status=status, id_embarcacao=1,
   id_audio=id_audio, id_arquivo=id_arquivo, tipo_arquivo=tipo_arquivo, id_categoria=id_categoria)
  
  tutorial.save()

def consultaTutorial():
  tutorial = Tutoriais.query.all()
  print(tutorial)


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
  consultaTutorial()
