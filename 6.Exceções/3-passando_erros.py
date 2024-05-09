#Indicando Tipos de Erros

meses = [1,2,3,4,5,6,7,8,9,10,11,12]

# Erro de index error, quando o index esta fora da faixa
print(meses[15])

# Tratando o erro
try:
    print(meses[15])
except IndexError as erro:
    print('Favor acessar um indice válido')

    #Se precisar pode printar o erro para ajudar na tratativa
    print(erro)



