# Funções com argumentos dinâmicos

# Funções com argumentos dinamicos são identificadas como *args

#Para quando precisamos passar n valores na função
# Usar o * com parametro que vai receber os n valores,
# Outros parametros precisam ser nomeados, no caso o b
# Os n valores são passados para a função em formato de tupla
def somar(*valores, b):
    print(valores)
    # Como é uma tupla, é preciso um laço para iterar
    for valor in valores:
        b += valor
    print(b)

somar(5,6,7,8, b=5)

