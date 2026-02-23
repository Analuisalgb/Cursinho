from random import randint
jogador = 20
robo = 0
while jogador != robo:
    robo = randint(0, 5)
    jogador = int(input('Informe um valor de 0-5: '))
    if not 0<= jogador <= 5:
        print('Jogada inválida! Tente novamente')
    else:
        print(f'Eu não acertei, você colocou {jogador} e eu coloquei {robo}!')
print(f'Eu acertei! Você colocou {jogador} e eu também coloquei {robo}!')