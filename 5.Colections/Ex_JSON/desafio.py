# Imprimir o e-mail do usuário com id 2
# Imprimir a city do usuário com id 1
# Imprimir o total do pedido do usuário com id 2

import json
path = '/home/rafael/Python/Pythonista/5.Colections/Ex_JSON/'


with open(f'{path}desafio.json', encoding='utf-8') as desafio_json:
    dados = json.load(desafio_json)
    # Item 1
    print(dados["user"][1]["email"])
    # Item 2
    print(dados["user"][0]["address"]["city"])
    # Item 3
    print(dados["user"][1]["orders"][0]["total"])

