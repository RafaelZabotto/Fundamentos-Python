# Herança Multinivel (evitar usar)

# Até 2 níveis é aceitável

# Não faça isso
class Veiculo:
    pass
class VeiculoDeRodas(Veiculo):
    pass
class Carro(VeiculoDeRodas):
    pass
class CarroEletrico(Carro):
    pass
class CarroEletricoDuasPortas(CarroEletrico):
    pass