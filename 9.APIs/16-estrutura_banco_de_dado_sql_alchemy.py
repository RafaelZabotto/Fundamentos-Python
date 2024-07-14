# Como não foi instalado os pacotes e db, o programa não vai rodar, aqui tem apenas o script

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar um API flask
app = Flask(__name__)

# Criar uma instancia de SQLAlchemy
app.config['SEXRET_KEY'] = 'FSD2323f#@#%^$A'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://blog.db'

db = SQLAlchemy(app)
db:SQLAlchemy

# Definir estrutura da tabela Postagem sem uso do codigo SQL
class Postagem(db.Model):
    __tablename__='postagem'
    id_postagem = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# Definir tablea Autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

#Executar o comando para criar o banco de dados
with app.app_context():
    db.drop_all()
    db.create_all()

    # Criar usuários administradores
    Autor(nome='rafael', email='rafael@rmail.com', senha='123456',admin=True)
    db.session.add(autor)
    db.session.commit()
