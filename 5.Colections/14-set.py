# SET
# É um tipo mutavel, pode receber mais elementos, mas devem ser unicos

#Lista
numeros = [2,2,5,8]
frutas = {'maça', 'uva', 'banana', 'maça', 'morango'}

# Convertendo para SET
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)

# Adicionando novos valores
set_numeros.add(10)
print(set_numeros)

#Conjuntos
numeros1 = [2,2,5,8]
numeros2 = [2,2,3,9]

a = set(numeros1)
b = set(numeros2)

# Vai mostrar os elementos q estão em a e b, mas não nos dois ao mesmo tempo
print(a.symmetric_difference(b))

# Interceção - o que esta presente nos dois conjuntos
print(a.intersection(b))

# União - removendo as duplicidades.
print(a.union(b))
