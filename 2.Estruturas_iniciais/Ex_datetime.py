# Calcular quantos dias faltam até o aniversário

from datetime import datetime

data_dia_mes = input('Qual é o dia e o mês do seu aniversário? ')
data_aniversario = data_dia_mes + '/' + str(datetime.now().year)
print(data_aniversario)

#construindo data atual
data_atual = str(datetime.now().day) + '/' + str(datetime.now().month) + '/' + str(datetime.now().year)

dias_restantes = datetime.strptime(data_aniversario, '%d/%m/%Y') - datetime.strptime(data_atual, '%d/%m/%Y')

print(dias_restantes.days)