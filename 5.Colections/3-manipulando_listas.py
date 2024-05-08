#Manipulando valores dentro das listas

valores = [1,2,3,4,5,6,7,8,9,10]
anos = [2020, 2030, 2040, 2050]

#Adicionado valroes no final da lista
valores.append(11)
print(valores)

#Unir listas
valores.extend(anos)
print(valores)

#Adicionar listas
nova_lista = valores + anos
print(nova_lista)

#Inserir um novo valor dentro da lista
print(anos[1])
anos.insert(2,2031)

print(anos)

#Extrair com base no index
anos_2020 = anos.pop(0)
print(anos_2020)

#Remover item da lista

anos.remove(2050) #por valor
del anos[1] #por index

print(anos)


#Contando a ocorrencia de um valor
print(valores.count(2))

#Resetar listas

valores.clear()
print(valores)