# Meu primeiro programa
from random import randint  # importa a função de gerar número aleatório

print("Jogo de Dados:")

dado1 = randint(1, 6)  # gera um número entre 1 e 6 aleatoriamente
print("dado1:", dado1)

dado2 = randint(1, 6)
print("dado2:", dado2)

dado3 = randint(1, 6)
print("dado2:", dado3)

dado4 = randint(1, 6)
print("dado4:", dado4)

Jogador1 = dado1 + dado2
Jogador2 = dado3 + dado4

print('Jogador1:', Jogador1)
print('Jogador2:', Jogador2)

if Jogador1 > Jogador2:
    print("Jogador1 venceu!")
else:
    if Jogador2 > Jogador1:
        print("Jogador2 venceu!")
    else:
        print("Empate!")
