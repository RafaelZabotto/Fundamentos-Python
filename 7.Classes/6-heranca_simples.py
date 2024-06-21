#  Herança

# No python, por padrao a classe herda da classe object (mas fica oculto) 
class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels


    def tirar_foto(self):
        print(f'Camera {self.marca} com qualidade de {self.megapixels} megapixels')

# Vai herdar os atributos da Camera
class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        #O metodo super faz com que as informações indicadas sejam passadas pela classe pai
        super().__init__(marca,megapixels)
        self.quatidade_de_cameras = quantidade_de_cameras

    def aplicar_filtro(self,filtro):
        print(f'Aplicando filtro {filtro}')

# Sobreescrever metodos da classe pai
# Só criar o metodo com o mesmo nome

    def tirar_foto(self, camera_a_utilizar):
        print(f'blablabla')
    

camera_celular = CameraCelular('Sony', '16mp', 4)
camera_celular.aplicar_filtro('Azul')
camera_celular.tirar_foto(2)