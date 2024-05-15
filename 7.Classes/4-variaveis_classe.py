# DEfinir variáveis de classe

#Abaixo só temos variáveis de instancia e elas não são acessiveis a não ser que instaciamos a classe
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Estou ligando o computador agora')

# Computador.marca não funciona pq não instaciamos\

# Isso funciona
computador = Computador('Dell', '8gb', 'NVIDIA')
computador.marca = 'ASUS'
print(computador.marca)



# Declarando uma váriavel de classe
class Computador:

    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Estou ligando o computador')


# Agora é possivel acessar a variável sem instaciar a classe e ela pode ser modificavel conforme o escopo
Computador.sistema_operacional = 'Linux'
print(Computador.sistema_operacional)


computador.ligar()




