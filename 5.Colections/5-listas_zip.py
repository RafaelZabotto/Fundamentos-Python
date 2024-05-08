from itertools import zip_longest

#Processando muitas listas com o ZIP

a_lista = ["A", "B", "C", "D", "E"]
b_lista = [1, 2, 3, 4, 5,]

for a,b in zip(a_lista, b_lista):
    print(a)
    print(b)

produtos = [ ]
precos_produtos = [250, 150, 220, 550, 50]


for a,b in zip (produtos, precos_produtos):
    print(f"Salvando {a} valor R$ {b}")

titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4', 'Titulo 5']
descricoes = ['Descrição 1', 'Descrição 2', 'Descrição 3']

for a,b in zip_longest(titulos, descricoes):
    print(f"Encontramos o {a} com a descrição: {b}")