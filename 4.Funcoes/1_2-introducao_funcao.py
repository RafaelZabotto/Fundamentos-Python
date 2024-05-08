 # Sobre funções e criando 

# def nome_da_funcao(parametros):
#     comandos

def dar_boas_vindas():
    print('Bem vindo!')

dar_boas_vindas()


# Recebendo parametros, passando argumentos

def dar_boas_vindas_personalizada(nome):
    print(f"Bem vinda: {nome}")


dar_boas_vindas_personalizada('Rafael')

# Usando um valor padrão caso não seja passado um valor personalizado
# O python não aceita parametros padrãos no começo da lista de argumentos, por isso se tiver mais de 1, ele deve ser declarado no final
def apresentar_lugar(horario_de_funcionamento, lugar='nossa loja'):
    print(f'Conheça {lugar}, horario de funcionamento das {horario_de_funcionamento}')

apresentar_lugar()