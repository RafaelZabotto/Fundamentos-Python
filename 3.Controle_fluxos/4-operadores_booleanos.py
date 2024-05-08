# Operadores Booleanos e Comparações

idade = 21
possui_convite = False
filho_do_dono = True
print((idade > 21) and (possui_convite == True)) # False
print(idade >= 21  and possui_convite == True)

#maior de 21 e possui convite ou seja filho do dono

print(idade > 21 and possui_convite == True or filho_do_dono == True)


#Outros exemplos

maior_de_idade = True
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False

#Contratar alguem maior de idade e com carteira de motorista
print(maior_de_idade == True and possui_carteira_de_trabalho == True)

#Contratar  alguem que não possua veiculo proprio mas já tenha carteira de motorista
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)





