# Ignorando erro

internet = None

# Explicação

# O try irá testar se a ação não irá gerar erro
try:
    print('Fazendo conexão com a' + internet)

# O except será disparado caso o try falhar
except TypeError as error:
    print('Não há conexão com a internet')

# Em alguns casos a aplicação precisa finalizar e não ficar travado no except, nesse caso usamos o finally para encerrar
finally:
    print('Desfazendo a compra')


# Outro Exemplo

#Zero Division Error e Value Error, trantando mais de uam excessão.
try: 
    valor = int(input('Digite um valor'))
    print(valor / 0)
except ZeroDivisionError as error:
    print('Não é possivel dividir por zero')
except ValueError as error:
    print('Favor digitar apenas números')
finally:
    print('A opera;cão foi cancelada') 

