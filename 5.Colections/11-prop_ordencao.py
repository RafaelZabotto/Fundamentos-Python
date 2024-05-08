#ordenar por propriedade simples

nomes = ["Zack", "Camila", "Julius", "Cariza"]
valores = [31, 34, 65, 12, 71, 25, 15, 10, 5, 87,19]

nomes.sort()
valores.sort()

print(nomes)
print(valores)

#ordenação mais elaborada, usar biblioteca itemgetter
from operator import itemgetter

pessoas = [
    {'nome': 'John',
    'idade': 32,
    'nível_acesso': 2},
    {'nome': 'Carol',
    'idade': 18,
    'nível_acesso': 3},
    {'nome': 'Thomas',
    'idade': 45,
    'nível_acesso': 5},
    {'nome': 'Amanda',
    'idade': 23,
    'nível_acesso': 1}
]
pessoas.sort(key=itemgetter('nome'))
print(pessoas)

#para tuplas segue o mesmo esquema
produtos = [
    ('Celular', 750),
    ('Bicicleta', 1500),
    ('Microfone', 550)
]

produtos.sort(key=itemgetter(0))
#para ordenação decrescente use produtos.sort(key=itemgetter(0), reverse = True)
print(produtos)

#com matrizes

matriz = [
    [5, 10],
    [15, 21],
    [1, 5]
]

matriz.sort(key=itemgetter(0))
print(matriz)

