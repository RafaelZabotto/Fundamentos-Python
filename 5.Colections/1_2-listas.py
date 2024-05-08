# Listas 

precos = [10, 20, 30,40]
precos[2]


print(precos[2])

# para listas com muitos valores e vc quer acessar um valor especifico
print(precos[precos.index(40)])

# Listas Dinamicas

itens = [1,2.6, 'Ola', 'Café', True]

# Maneiras de gerar listas (Multiplicação de valores)

lista_de_noves = [9] * 10
print(lista_de_noves)

lista_de_Testes = ['Teste'] * 10
print(lista_de_Testes)

faica_de_numeros = list(range(30))
print(faica_de_numeros)

# Gerar a partir de strings

print(list('Bem-vindo ao treinamento'))

#Lista de listas(matriz)

matriz_de_nomes = [['Carol', 30], ['Marcus', 50]]

print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0]) 
print(matriz_de_nomes[1][0]) 