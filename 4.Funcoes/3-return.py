# Processar VS Retornar

#Exemplos
# Funções que apenas processa dados:
print('Olá!')

# Funções que retornam dados
cidade = input('Qual a sua cidade: ')

# Outro exemplo
# Processa dados
def exibir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)

# Retorna dados
# Nesse caso ela vai devolver um resultado para quem esta chamando ela
def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47

# Salvando o return da função em uma variável    
cotacao = obter_cotacao_do_dia('usd')

if cotacao > 5:
    print('Investir em ações americanas')
else:
    print('Cotação não favorável')




