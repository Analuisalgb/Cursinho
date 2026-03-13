from random import randint
from time import sleep
quantidade = int(input('Quantos jogos deseja que eu faça? '))
numver = 0
jogo = []

for c in range(1,quantidade+1):
    print(f'Jogo {c}:', end=' ')
    for c in range(0,6):
        numver = randint(1,60)
        while True:
            if numver not in jogo:
                jogo.append(numver)
                break
            else:
                numver = randint(1,60)

    print(sorted(jogo))
    sleep(1)
    jogo.clear()
