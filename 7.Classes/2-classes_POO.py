# para criar uma classe

class Computador:
    def __init__(self, marca,memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

# Criado instancia
# InformaçÕes - marca, mem ram, palca de video
computador1 = Computador('Asus','16gb','NVIDIA')
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)
