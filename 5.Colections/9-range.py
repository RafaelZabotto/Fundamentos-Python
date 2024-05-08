#Aprofundando na função range (geradores)

# print(type(range(30)))

#normal
for numero in range(30):
    print(numero)

print('-------------------------------------')

#com intervalo
for numero in range(10, 30):
    print(numero)

print('-------------------------------------')

#com intervalo e selecionando os pares
for numero in range(10, 30, 2):
    print(numero)

print('-------------------------------------')

#Criar listas rapidamente com o range
resultado = list(range(0, 201, 10))
print(resultado)