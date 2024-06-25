from carro import ligar_carro
from moto import ligar_moto


# O If __name__ é uma condicional
# O __name__ vai ser o identificador do arquivo que esta sendo processado manualmente, por exemplo digamos que esse script esta dividido em 3 arquivos.
# Um chamado app.py e os outros carro.py e moto.py. Quando der um run no app.py, o __name__ será o identificador desse arquivo, recebendo 


if __name__ == '__main__':
    print('Ligando veiculos')
    print(f'Estamos no arquivo {__name__}')




############# Arquivo Carro #######################

def ligar_moto():
    print('Ligar carro')

if __name__ == '__main__':
    print('Tirando carro da garagem')
    print(f'Estamos no arquivo {__name__}')



############# Arquivo Moto #######################

def ligar_moto():
    print('Ligar moto')

if __name__ == '__main__':
    print('Tirando moto da garagem')
    print(f'Estamos no arquivo {__name__}')