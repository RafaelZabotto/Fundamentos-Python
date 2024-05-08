# Loop While (laço while)

tentativas = 0 

while tentativas < 3:
    print('tente novamente')
    tentativas += 1

# Verificando Senha
senha = ''
while senha != '123456':
    senha = input('Digite sua senha')
print('Bem-vindo!')

# Recebendo nome do usuário

nome = ''

while nome == '':
    nome = input('Digite seu nome: ')
print(f'Bem vindo {nome}')

# Ver por do sol as 17:00

horario = 0 
while horario <= 17:
    print(horario)
    horario += 1
print('Hora de ir ver o por do sol')

# Contador regressiva
contador = 100

while contador >= 0:
    print(contador)
    contador -= 1
