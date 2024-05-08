# Controlando oq esta acontecendo dentro dos laços

# Continue - ignore oq esta passando no laço
# Só vai printar os pares e ignorar os ímpares
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        continue



# Break - interromper a iteração
# Interrompe a execução no primeiro caso que não satisfaça a condição
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        break

##################################
    
# Outros exemplos

# Vai exibir tudo, menos manga
frutas = ['Maçã', 'Manga', 'Laranja', 'Morango']
for fruta in frutas:
    if fruta == 'Manga':
        continue
    print(f'{fruta} adicionada a dieta')

# Vai exibir até manga e depois pára
frutas = ['Maçã', 'Manga', 'Laranja', 'Morango']
for fruta in frutas:
    if fruta == 'Manga':
        break
    print(f'{fruta} adicionada a dieta')

