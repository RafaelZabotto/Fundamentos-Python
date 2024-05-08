import random

# Desafio 1 - Simular a opção de jogar uma moeda e resultar em cara ou coroa

opcoes_moeda = ['cara', 'coroa']
print(random.choices(opcoes_moeda))

# Desafio 2 - Fazer um sorteio entre 5 nomes em uma lista de nomes

nomes = ['Rafael', 'Cariza', 'Daniel', 'Nicolas', 'Michelly']
print(random.choices(nomes))

# Desafio 3 - Escolher aleatóriamente um número de 10-100
print(random.randint(10, 100))