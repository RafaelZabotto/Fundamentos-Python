from datetime import datetime

print(datetime.now().now)
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

#Criar uma data
lancamento_app = datetime(2021,5,28)
print(lancamento_app)

#Quero receber a data lançamento do meu aplicativo
data_de_lancamento = datetime.strptime(input('Quando devemos lançar o app?'),'%d/%m/%Y') # formantando para data
print(data_de_lancamento)
print(type(data_de_lancamento))

#Intervalo entre datas

data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)

