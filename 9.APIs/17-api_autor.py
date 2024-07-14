# Como não foi instalado os pacotes e db, o programa não vai rodar, aqui tem apenas o script
# Esse código estava iniciamente inserido no arquivo 6-consultando_api.py

from flask import Flask, jsonify, request

# Iniciando App
app = Flask(__name__)

@app.route('/autores')
def obter_autores():
    pass

@app.route('/autores/<int:id_autor>', methods=['GET'])
def obter_autor_id(id_autor):
    pass

@app.route('/autores', methods=['POST'])
def novo_autor():
    pass

@app.route('/autores/<int:id_autor>', methods=['PUT'])
def alterar_autor(id_autor):
    pass

@app.route('/autores/<int:id_autor>', methods=['DELETE'])
def excluir_autor(id_autor):
    pass

app.run(port=5000, host='localhost', debug=True)