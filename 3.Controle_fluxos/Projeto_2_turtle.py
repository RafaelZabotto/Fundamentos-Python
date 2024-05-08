from turtle import Turtle

turt = Turtle()

turt.speed(1)

#While mestre com true
while True:
    
    sentido = input('Deseja movimentar para frente (F) ou para trás (T)?: ')
    distancia = int(input('Qual a distancia que a turtle deve percorrer (em pixels)?: '))

    if sentido.upper() == 'F':
        turt.forward(distancia)
    elif sentido.upper() == 'T':
        turt.backward(distancia)
    else:
        print('Valor inválido')

    rotacao = input('Deseja rotacionar para direita (D) ou para esquerda (E)?: ')
    angulo = int(input('Quantos pixels a turtle deve ser rotacionada (90 = 90 graus)?: '))

    if rotacao.upper() == 'D':
        turt.right(angulo)
    elif rotacao.upper() == 'E':
        turt.left(angulo)
    else:
        print('Valor inválido')

    acao = input("Deseja continuar? S ou N: ")
    
    if acao.upper() == "S":
        continue
    else:
        break 

# 1 movimentar para frente ou para trás
# 2 Quantos pixels movimentar
# 3 Rotacionar para direita ou esquerda
# 4 Quantos pixels devem ser rotacionados
# 5 Continuar andando?
