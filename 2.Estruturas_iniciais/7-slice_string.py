teclado = 'Teclado'

#Acessando letras da string
print(teclado[2]) # vai retornar a letra C

#Acessando letra a
print(teclado[4])

#Acessando o ultimo caracter da string
print(teclado[-1])

#Acessando um caracter desejado
print(teclado.index('l'))

#Acessando partes de uma string
link = 'facebook.com/devaprender'
print(link[0])
print(link[-1])
print(link[0:5]) #aonde vai iniciar e finalizar
print(link[0:]) # do começo e ir até o final
print(link[-5:]) # até a posição 5 a partir do final
print(link[5:])
print(link[:-5]) # até a posição 5 a partir do inicio

#Buscando caracteres que estão sendo repetidos
frase = 'Clean code'

print(frase.rindex('C')) #Usando o rindex