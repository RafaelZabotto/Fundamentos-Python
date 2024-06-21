#Herança Multipla
# Permite unir metodos e funconalidades de classes em uma só

class Pessoa:
    nome = 'Sou uma pessoa'

class Profissional:
    nome = 'Sou um profissional'

class AtorProfissional(Pessoa, Profissional):
    pass

print(AtorProfissional.nome)
# a ordem de resolução no Python segue o MRO, é possivel acessar a ordem pelo comando
print(AtorProfissional.mro())

