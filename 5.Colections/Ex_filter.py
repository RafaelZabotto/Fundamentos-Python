# Desafio
# Filtar vagas com salario acima de R$2500

vagas = [ 
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]


def salario_alto(vagas):
    if vagas[1] > 2500:
        return True
    else:
        return False
    
print(list(filter(salario_alto, vagas)))
