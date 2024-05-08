# Argumentos Posicionais
# Os argumentos devem ser passados na mesma ordem estabelecida na definição da função
# Ou seja, a posição importa

def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} esta no valor de? {preco}')

exibir_preco('Iphone', 5000)

# Argumentos nomeados
# É independente da ordem
# Ambas as chamadas abaixo irão funcionar normalmente
exibir_preco(nome_produto='Iphone', preco=5000)
exibir_preco(preco=5000, nome_produto='Iphone')


# Solicitar na def da função que os argumentos devem ser passados de forma nomeada
# Usar o *
# Todos os parametros após o * devem ser nomeados
def exibir_preco2(nome_produto,*,preco):
    print(f'{nome_produto} esta no valor de? {preco}')

exibir_preco2('Iphone', preco=5000)


