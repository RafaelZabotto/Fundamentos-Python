# Como ler arquivos JSON
# JSON (Javascript Object Notation)

import json

path = '/home/rafael/Python/Pythonista/5.Colections/15-JSON/'

with open(f'{path}/usuarios1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter um arquivo json para string
    print(data['nome'])
# O retorno é um dicionario, por isso no debug console é possivel acessar as informações pela chave
    
#Exemplo com arquivo usuários 2
with open(f'{path}/usuarios2.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter um arquivo json para string
    print(data["permissões"][1])
    # Acessar segundo nivel de informações

# Exemplo 3 - acessando 2 niveis dentro do json
with open(f'{path}/usuarios3.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter um arquivo json para string
    print(data["usuários"][0]["telefone"])
    print(data["usuários"][1]["admin"])


# Exemplo 4 - acessando mais niveis dentro do json
with open(f'{path}/usuarios4.json') as arquivo_json:
    data = json.load(arquivo_json) # Converter um arquivo json para string
    print(data["usuários"][0]["plano"]["preco"])

    


