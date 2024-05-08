import os


# # Primeiro crie 3 listas
#  * Uma lista que contem 5 frutas
#  * Uma lista que contem 5 cores
#  * Uma lista que contem 5 linguagens de programação
# # Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
# # Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
# # Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
# # Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.

frutas = ['banana', 'pera', 'maca', 'laranja', 'melancia']
cores = [ 'amarelo', 'azul', 'vermelho', 'verde', 'branco']
linguagens = [ 'java', 'php', 'c', 'python', 'scala']

# Desafio 1

with open('frutas.txt', 'w', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

# Desafio 2

with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

# Desafio 3
with open('frutas.txt', 'a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(cor + os.linesep)

# Desafio 4
with open('Top 5 Linguagens.txt', 'a', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)

