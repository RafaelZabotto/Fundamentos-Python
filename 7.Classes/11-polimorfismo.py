# Funções que se adaptam conforme os dado passado

# Exemplo usando o operador de +
# Com inteiros
print(10+30)
# Com Strings
print('olá ' +  'Dev!')

# No caso de funções

class Carro:
    def ligar(self):
        print('Ligando o carro')

class Moto:
    def ligar(self):
        print('Ligando a moto')

def iniciar(veiculo):
    veiculo.ligar()

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)

# No caso o metodo iniciar é polimorfico

