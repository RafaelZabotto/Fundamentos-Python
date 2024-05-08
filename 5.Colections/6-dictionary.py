# Divcionarios

#lista normal
pessoa = ['Carol', 18, 1.60, 'Mike', 50, 1.80]

#Dicionario - padrão chave/valor

dicionario_pessoas = {
    'nome': 'Carol',
    'idade': 18,
    'altura': 1.60
}

print(dicionario_pessoas)

#Outra forma de criar um dicionario

dicionario_pessoas_2 = dict(nome='Carol', idade=18, altura=1.60)

print(dicionario_pessoas_2)

#acessar dados dentro de um dicionario

print(dicionario_pessoas_2['nome'])

#printar chaves disponíveis
print(dicionario_pessoas_2.keys())

#só valores
print(dicionario_pessoas_2.values())

#chaves e valores
print(dicionario_pessoas_2.items())

#Iterar sobre um dicionario
for item in dicionario_pessoas_2.values():
    print(item)