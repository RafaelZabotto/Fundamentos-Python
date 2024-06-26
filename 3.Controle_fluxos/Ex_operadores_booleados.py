# ​# Desafio 🥇

# Quero que você defina as seguintes variáveis, inicialmente todas como False, a ideia aqui não é de se importar com os valores dentro dessas variáveis, mas sim como montar condicionais.

# possui_passaporte = False
# passagem_comprada = False
# menor_de_idade = False

# E Crie as seguintes condições usando o que acabou de ver e imprima o resultado na tela. Tente fazer cada condição e depois veja a solução no final deste aula.
# Uma pessoa só pode viajar se possuir  passaporte e tiver a passagem comprada e não for menor de idade
# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade


possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

# Condição 1

print(possui_passaporte == True and passagem_comprada == True and menor_de_idade == False)

# Condição 2 

print((possui_passaporte == True or passagem_comprada == True) and menor_de_idade == False)

# Condição 3

print((possui_passaporte == False or passagem_comprada == True) and menor_de_idade == False)

# Condição 4

print((possui_passaporte == False or passagem_comprada == False) and menor_de_idade == True)