# Funções com arguementos nomeados dinamicos

# Funções com nomeados dinamicos são identificadas como **kwargs

# Para quando precisamos nomear n argumentos
# Para quando precisamos receber n argumentos nomeados usamos **
# Gera uam tupla tmb
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' ' 
    print(frase)


concatenar(a='Nós', b='Somos', c='Pythonistas', d='Profissionais')

# Em resumo

# Args => *algumacoisa
# kwargs => **algumacoisa
# Sempre recebem n arguemtnos
# Sempre geram tuplas

# Exemplo completo

def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

fazer_calculo('Jeff', 4,6,3,7, a=1,b=2,c=3)
        #posicional   #args    #kwargs