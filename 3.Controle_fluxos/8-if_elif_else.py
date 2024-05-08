# Condicionais e Controles de Fluxo

trabalho_terminado = True

if trabalho_terminado == True:
    print('Posso sair!')
else:
    print('Não posso sair agora')

#################################
    
numero_atrasos = 2

if numero_atrasos >= 3:
    print('Vá para a diretoria')
elif numero_atrasos == 2:
    print('Essa é a sua segunda falta')
elif numero_atrasos == 1:
    print('Essa é sua primeiera falta')
else:
    print('Pode entrar')


####################################
    
# Outro exemplo
    
velocidade = 55

if velocidade <= 50:
    print('Não foi multado')
elif velocidade >= 51 and velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
     print('Levou multa de 7 pontos')

####################################
     
# Utilizando o chaining para facilitar a comparação de faixas de valores
     
velocidade = 55

if velocidade <= 50:
    print('Não foi multado')
elif 51 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
     print('Levou multa de 7 pontos')
 