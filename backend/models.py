from sqlalchemy import create_engine, Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os

# esta classe é chamada pelo flask run
# print('\n\nteste6\n\n')

# cria o banco no diretório do app.py
stringDaEngine = 'sqlite:///' + os.path.join(os.path.dirname(__file__),'database.db')
engine = create_engine(stringDaEngine, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit = False, bind = engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Metodos():
  def __repr__(self):
    return "<{} : {}>".format(self.__class__.__name__,self.nome)

  def save(self):
    db_session.add(self)
    db_session.commit()

  def delete(self):
    db_session.delete(self)
    db_session.commit()
  
  def finaliza(self):
    db_session.commit()
    db_session.close()

class Embarcacoes(Base, Metodos):
  __tablename__ = 'embarcacoes'
  id = Column(Integer, primary_key = True)
  nome = Column(String)
  tutorial = relationship('Tutoriais')

  # def __repr__(self):
  #   return "<Embarcacoes {}>".format(self.nome)


class Arquivos(Base, Metodos):
  __tablename__ = 'arquivos'
  id = Column(Integer, primary_key = True)
  nome = Column(String)
  url = Column(String)
  tutorial = relationship('Tutoriais')

  # def __repr__(self):
  #   return "<Arquivos {}>".format(self.nome)



class Categorias(Base, Metodos):
  __tablename__ = 'categorias'

  id = Column(Integer, primary_key = True)
  nome = Column(String)
  status = Column(Boolean)
  tutorial = relationship('Tutoriais')

  # def __repr__(self):
  #   return "<Categorias {}>".format(self.nome)

class Audios(Base, Metodos):
  __tablename__ = 'audios'

  id = Column(Integer, primary_key = True)
  nome = Column(String(50))
  # id_embarcacao = Column(Integer)
  url = Column(String)
  tutorial = relationship('Tutoriais')

class Tutoriais(Base, Metodos):
  __tablename__ = 'tutoriais'

  id = Column(Integer, primary_key = True)
  nome = Column(String(20))
  descricao = Column(String(100))
  status = Column(Boolean)
  status_categoria = Column(Integer)
  id_embarcacao = Column(Integer, ForeignKey('embarcacoes.id'))
  id_audio = Column(Integer, ForeignKey('audios.id'))
  id_arquivo = Column(Integer, ForeignKey('arquivos.id'))
  id_categoria = Column(Integer, ForeignKey('categorias.id'))
  tipo_arquivo = Column(String(4))
  # Relacionamentos
  arquivo = relationship("Arquivos")
  categoria = relationship("Categorias")
  embarcacao = relationship("Embarcacoes")
  audio = relationship("Audios")

  # def __repr__(self):
  #   return "<Tutorial {}>".format(self.nome) + '\n' + 'descrição do tutorial: {}'.format() + '\n' + 'status do tutorial: {}'.format(status) + '\n' + 'nome da embarcação: ' + 'teste'

def init_db():
  Base.metadata.create_all(bind = engine)

if __name__ == "__main__":
  init_db()
