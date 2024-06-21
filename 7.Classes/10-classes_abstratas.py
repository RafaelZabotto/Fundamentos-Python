# Classes Abstratas
# Cria um contrato(esqueleto) -> que deve ser implementado na classe que a herda
# É Obrigatorio a implementação das funções das classes abstratas para que elas funcionem

from abc import ABC, abstractmethod

class Camera(ABC):
    @abstractmethod
    def definir_tamanho_lente(self, tamanho):
        pass

class CameraProfissional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print(f'Alerando a lente para {tamanho}')

cameraProfissional = CameraProfissional()
cameraProfissional.definir_tamanho_lente(5)