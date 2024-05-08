# Map 

# Criando listas com loops
numeros = []

for numero in range(10):
    numeros.append(numero)
print(numeros)

# Criando Com MAP

nomes = [ 'Larissa', 'Rafael', 'Marcus', 'John']

def aprovar_pessoa(nome):
    return nome + ' Aprovado'

# O resultado do MAP sempre será um map, para ficar legivel é preciso converter pra list
print(list(map(aprovar_pessoa, nomes)))





