#Tuplas - itens que não podem ser alterados

site1 = 'youtube.com'
site2 = 'instagram.com'
site3 = 'facebook.com'

# Criação de tuplas
sites = ('youtube.com', 'instagram.com', 'facebook.com')
valores = (23, 54, 67, True)

#A tupla é identificada pelos ()
#União de tuplas
dados_do_sistema = sites + valores
print(dados_do_sistema)

#Acesso de valores das tuplas
print(dados_do_sistema[2])
print(sites)
print(valores)


print(type(dados_do_sistema))
