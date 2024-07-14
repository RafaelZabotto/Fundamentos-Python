from flask import Flask, jsonify, request

# Iniciando App
app = Flask(__name__)

postagens = [
    {
        'titulo': 'Minha História',
        'autor': 'Amanda Dias'
    },
    {
        'titulo': 'Novo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'titulo': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    }
]


# Rota padrão - GET http://localhost:5000/
@app.route('/')
def obter_postagens(): 
    return jsonify(postagens)

# Rota exclusiva - GET com ID http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>',methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

# Rota de criação de recurso - POST http://localhost:5000/postagem/
@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json() # esse comando serve para pegar a requisição enviada
    postagens.append(postagem)

    return jsonify(postagem, 200)

# Rota para alteração de recursos - PUT http://localhost:5000/postagem/0
@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice],200)

# Rota de exclusão - DELETE http://localhost:5000/postagem/0
@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice] 
            return jsonify(f'Foi excluido a postagem {postagens[indice]}', 200)
    except:
        return jsonify(f'Não foi possivel encontrar a postagem para exclusão', 404)

app.run(port=5000, host='localhost', debug=True)