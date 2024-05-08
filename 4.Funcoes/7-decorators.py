# Decorators - executar funções dentro de outras funções

# Preparação para entender o conceito

from datetime import datetime

def depositar_dinheiro():
    print('depositando dinheiro')

    def depositando_dolar():
        print('Depositando dolares')
    
    def depositando_reais():
        print('Depositando reais')

    depositando_dolar()
    depositando_reais()

# Note que a unica forma de acessar as funções depositar dolar e reais é chamando a depositar dinheiro
depositar_dinheiro()

def pai(numero):
    def filho_1():
        print('Sou filho 1')
    def filho_2():
        print('Sou filho 2')
    if numero == 1:
        return filho_1 # Nesse caso estamos retornando a referencia da função e não a função propriamente dita, por isso não se usa ()
    
resultado = pai(1) # Agora a referencia da função esta salva na variavel resultado
resultado() # Quando executamos essa var como função, retorna a função.

################################################################################


# Decorators
# Mecanismo que consegue controlar eventos antes e depois da execução de funções

# Método abaixo mostra como funciona
def meu_decorator(funcao):
    def wrapper(): # Pode ser qualquer outro nome
        print('antes')
        funcao()
        print('Depois')
    return wrapper

def parabenizar():
    print("Parabens!!!!")

resultado = meu_decorator(parabenizar)
resultado()

# Metodo mais simplificado
def meu_decorator(funcao):
    def wrapper(): # Pode ser qualquer outro nome
        print('antes')
        funcao()
        print('Depois')
    return wrapper

@meu_decorator
def parabenizar():
    print("Parabens!!!!")

parabenizar()
