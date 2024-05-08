# Desafio 1
# Ao chegar em Rap, o mesmo não deve ser impresso na tela

estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']

for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(estilo)

# Desafio 2
# Ao chegar em Rock, a execução deve ser interrompida
    
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)