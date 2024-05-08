# Desafio de argumentos

# Definição da função
# Primeiro argumento posicional
# Segundo e terceiro argumento nomeados 
def gerar_objeto_personalizado(cor,*,altura, formato):
    print(f'cor {cor}, altura {altura}, formato {formato}')

gerar_objeto_personalizado('amarelo', altura=1.70,formato='triangulo')
