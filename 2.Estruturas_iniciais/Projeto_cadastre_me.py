from datetime import datetime
import math
import random


#Modulo 1 - Dados

nome = input("Digite seu nome: ")
idade = int(input('Digite sua idade: '))
hora_registro = datetime.today().strftime("%d/%m/%Y")
cartoes = ['R$50,00','R$250,00','R$120,00']

cartao = random.choice(cartoes)

aniversario = datetime.strptime(input('Digite sua data de aniversário: '), '%d/%m/%Y')

#Modulo 2 - Exibição

print(f"Olá {nome}, seu registro foi concluído com sucesso no dia {hora_registro}.")
print(f"Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}.")