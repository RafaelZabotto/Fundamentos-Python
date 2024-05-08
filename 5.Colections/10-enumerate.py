#Enumerate

# enumerate é usado para percorrer listas

for indice, numero in enumerate(range(1, 11), 0):
    print(indice, numero)
    if indice == 5:
        print("Estamos na metade da lista")

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5',]

for indice, nome in enumerate(nomes, 1):
    print(indice, nome)
    if indice == 3:
        print("Já temos 3 pessoas registradas")

