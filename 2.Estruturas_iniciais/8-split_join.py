frase = 'Olá, bem-vindo a este treinamento!'

print(frase.split()) #vai criar uma lista de strings com separação pelo espaço
print(frase.split(',')) #vai criar a lista separando na virgula
print(frase.split('-')) #vai criar a lista separando no traço

nomes = 'jhonatan, rafael, carol, amanda, jefferson'

print(nomes.split()) #separação nos espaços em branco
print(nomes.split(',')) #separação nas virgulas

hashtags = 'music #guitar #gamer #coder #python'

print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3)) #vai separar até o terceiro elemento

# Concatenar strings

hashtag_separadas_por_espaco = hashtags.split(' ')

print(hashtag_separadas_por_espaco)
print(','.join(hashtag_separadas_por_espaco)) #vai colocar todos em um string unico separado por virgula
print('.'.join(hashtag_separadas_por_espaco)) #vai colocar todos em um string unico separado por ponto
print(' '.join(hashtag_separadas_por_espaco)) #vai colocar todos em um string unico separado por espaço


