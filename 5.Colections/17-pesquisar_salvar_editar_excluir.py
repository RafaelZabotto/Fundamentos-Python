import os

# COMO CRIAR E MODIFICAR ARQUIVOS:
# 'w'  -> Usado somente para escrever algo
# 'a'  -> Usado para acrescentar algo
# 'r'  -> Usado somente para ler algo
# 'r+' -> Usado para ler e escrever algo


# Criando arquivos
# Não é possivel adicionar informações novas, se tentar ele sobrescreve
with open('celulares.txt', 'w') as arquivo:
    arquivo.write('Celular 1')

# Acrescentando 
with open('nomes.txt', 'a', newline='') as arquivo:
    arquivo.write('amanda' + os.linesep)

# Outro exemplo para acrescentar
nomes = [ 'lucas', 'carol', 'jeff', 'douglas']

with open('nomes.txt', 'a', newline='') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)

# Acrecentando numeros, mas só str é aceito, por isso precisa converter
numeros = [1,2,3,4,5,6]
with open('numeros.txt', 'a', newline='') as arquivo: 
    for numero in numeros:
        arquivo.write(str(numero) + os.linesep)

# Para ler o conteudo do arquivo
with open('nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

# Para ler ou escrever algo novo
with open('numeros.txt', 'r+') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('9000')



