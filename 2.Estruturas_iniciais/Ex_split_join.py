frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camila'

# 1 - Transformar a frase1 em uma lista de palavras e guardar o resultado na var palavras1

palavras1 = frase1.split()

# 2 - Transformar a frase2 em uma lista de palavras e guardar o resultado em uma var chamada palavras2

palavras2 = frase2.split(',')

# 3 - Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console

print(','.join(palavras1))

# 4 - Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camila". Imprima o resultado no console

print(' & '.join(palavras2))

