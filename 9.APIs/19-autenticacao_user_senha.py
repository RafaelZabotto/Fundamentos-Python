# Inserindo autenticação de user e senha para deixar rotas mais seguras, restringindo-as a apenas usuários autenticados.
# Token de autenticação

# Exemplo: construindo uma API para baixar PApeis de Parede Premium
# papeldeparede.com/download/1
# Autenticação por Token JWT
# Token = 'SF@#T#TASDAS sdf !83475#@ASFAS'
# papeldeparede.com/login


from flask import Flask, jsonify, request, make_response
from estrutura_banco_de_dado_sql_alchemy import app
import json
import jwt 
from datetime import datetime, timedelta
from functools import wraps

# Função para utilziar o token gerado em cada requisição obrigatória da API
def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # verificar se um tokem foi enviado
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token: 
            return jsonify({'mensagem': 'Token não foi incluído!'}, 401)
        # Se temos um token, validar acesso consultado o BD
        try:
            resultado = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            autor = Autor.query.filter_by(id_autor=resultado['id_autor']).first()
        except:
            return jsonify({'mensagem': 'Token é inválido'}, 401)
        return f(autor, *args, **kwargs)
    return decorated

@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Login inválido', 401, {'WWW-Authntucate':'Basic realm="Login Obrigatório"'})
    # Autor não foi importado, portanto o codigo não vai rodar
    usuário = Autor.query.filter_by(nome=auth.username).first()
    if not usuario:
        return make_response('Login inválido', 401, {'WWW-Authntucate':'Basic realm="Login Obrigatório"'})
    # Se o usuario atender os requisitos, é liberado o seu acesso e gerado um token
    if auth.password == usuario.senha:
        token = jwt.encode({'id_autor': usuario.id_autor,'exp': datetime.now(datetime.UTC) + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token':token})
    return make_response('Login inválido', 401, {'WWW-Authntucate':'Basic realm="Login Obrigatório"'})

# Uso da autentição de token nas rotas, utilizando a rota de obter_autores

@app.route('/autores')
@token_obrigatorio
# Como estamos usando o decorador do token, é obrigatorio passar o autor como parametro
def obter_autores(autor):
    pass