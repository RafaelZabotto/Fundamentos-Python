# Desafio de requisições em uma api de musicas
from flask import Flask, jsonify, request

# Inicio do App
app = Flask(__name__)

cancoes = [
    {
        'cancao': 'Eons',
        'estilo': 'Lo-Fi'
    },
    {
        'cancao': 'Numb',
        'estilo': 'Rock'
    },
    {
        'cancao': 'Leão',
        'estilo': 'Sertanejo'
    },
    {
        'cancao': 'Poker Face',
        'estilo': 'Pop'
    },
    {
        'cancao': 'Blue Dream',
        'estilo': 'Anime Song'
    }
]

# GET
@app.route('/')
def lista_cancoes():
    return jsonify(cancoes)
    

# GET by ID
@app.route('/cancao/<int:indice>', methods=['GET'])
def lista_cancao_especifica(indice):
    return jsonify(cancoes[indice])


# POST
@app.route('/cancao/', methods=['POST'])
def insere_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify(cancao, 200)


# PUT
@app.route('/cancao/<int:indice>', methods=['PUT'])
def atualiza_cancao(indice):
    cancao_atualizada = request.get_json()
    cancoes[indice].update(cancao_atualizada)
    return jsonify(cancoes[indice],200)


# DELETE
@app.route('/cancao/<int:indice>', methods=['DELETE'])
def deleta_cancao(indice):
    try:
        if cancoes[indice] is not None:
            del cancoes[indice]
            return jsonify(f'Canção {cancoes[indice]} deletada', 200)
    except:
        return jsonify(f'Canção {cancoes[indice]} não encontrada', 404)


app.run(port=5000, host='localhost', debug=True)