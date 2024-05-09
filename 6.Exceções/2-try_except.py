# Tratando excessões
# Usando o try except

# O bloco abaixo possui uma brecha quando o user digita um valor não numerico
# isso ocasiona um erro, para evitar, usamos o try except

try:
    valor = int(input('digite um valor em dolares: '))
    print(valor * 5.25)
except:
    print('Digite um valor apenas em numeros')


