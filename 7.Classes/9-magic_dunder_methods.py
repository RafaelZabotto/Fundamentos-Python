# __(algum nome)__ -> metodos magicos (magic methods, dunder methods< underscore)
# São chamados assim pq não são chamados diretamente.

class Pessoa:
    def __init__(self):
        self.nome = 'Sou uma pessoa'
        self.habilidades = ['Habilidade 1', 'Habilidade 1', 'Habilidade 1']

    # Representação da classe
    def __repr__(self):
        return 'Classe Pessoa com propriedades nome e habilidades'

    # O que deve ser mensurado para determinar a quantidade daquela classe(chamda com metodo len(pessoa))
    def __len__(self):
        return len(self.habilidades)

    # REpresentação de string
    def __str__(self):
        return f'{self.nome} com as habilidades {self.habilidades}'

pessoa = Pessoa()
print(pessoa.nome)  
print(repr(pessoa))
print(len(pessoa))
print((pessoa))
print(dir(pessoa))