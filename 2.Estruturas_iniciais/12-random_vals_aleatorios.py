# Gerando valores aleatorios com o Random

import random

# gerando valor aleatorio em 0.0 e 1.0
print(random.random())

#gerando entre 4 e 10 com decimais
print(random.uniform(4,10))

#gerando entre 4 e 10 inteiros
print(random.randint(4,10))

# Escolher opção aleatorio dentro de uma lista
cores = ['verde', 'vermelho', 'azul']
print(random.choice(cores))

# Escolher mais de uma opção aleatorio dentro de uma lista
print(random.choices(cores, k=2))

# Embaralhar valores
cartas_de_baralho = ['carta1', 'carta2', 'carta3', 'carta4']
random.shuffle(cartas_de_baralho) # print precisa ser separado para ver os itens
print(cartas_de_baralho)


