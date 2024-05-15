# Métodos Comuns 
# Métodos de classe
# Métodos estáticos

# Metodos comuns - acessam propriedades da instancia por meio do self(obrigatório)
class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, self.sistema_operacional)

# Metodos de classe - não são tão usados, mas são uteis em cenários especificos, quando é preciso modificar a classe em si
# Ex. Loja que vende pcs com diferentes configs:
# Config p/ cliente de escitorio
# Config para clientes com uso intenso

    @classmethod
    def computador_escritorio(cls, memoria_ram): # o cls é uma convensão do python, indicando que estamos passando a classe inteira
        return cls('Dell', memoria_ram, 'Placa de Video - padrão')

    @classmethod
    def computador_uso_intenso(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Video - Alta Performance')
    
    # Metodos estáticos - não usam a instancia da classe através da self e não modificam as propriedades da classe atraves com cls
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False

# Instanciação do exemplo dos metodos de classe    
computador1 = Computador.computador_escritorio('8gb')
computador2 = Computador.computador_uso_intenso('16gb')

computador1.exibir_dados_do_computador()
print('#############')
computador2.exibir_dados_do_computador()

# Chama do metodo estatico
print(Computador.roda_programas_pesados(10))




    

