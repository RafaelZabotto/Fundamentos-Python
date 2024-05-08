#Recebendo dados do user

senha = input('Digite sua senha: ')
print(senha)
print(type(senha)) # str

# O resultado de um input sempre será um string
# Para que o input tenha outro tipo de valor, é preciso passar o cast na declaração do função

quantidade_de_filmes = int(input('Quantos filmes você já viu no mês?'))
print(type(quantidade_de_filmes)) # int