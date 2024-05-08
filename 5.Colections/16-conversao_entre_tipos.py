# Conversão entre tipos 

# Para int
idade = input("digite a idade")
print(int(idade) > 17)

# Para str
ano_publicacao = 2020
print('Este livro foi criado em' + str(ano_publicacao))

# Para float
altura = input('Qual é a altura da parede')
print(float(altura) > 2.50)

#Conversões entre coleções

saudacao = 'Hello'
print(list(saudacao))
print(set(saudacao))
print(tuple(saudacao))
print(list(range(30)))

numeros = [10,20,30,40]
print(set(numeros))
print(tuple(numeros))

# Para encontrar o tipo da variável
print(type(numeros))

