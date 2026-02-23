from random import randint
robo = -2
jogador = 15
jogador = int(input('Me diga um número de 0 a 10: '))
while jogador != robo:
    robo = randint(0, 10)
    if 0<= jogador <= 10:
        if robo != jogador:
            print(f'Eu não acertei! Eu disse {robo} e você {jogador}! Vamos de novo')
            jogador = int(input('Me diga um número de 0 a 10: '))
    else:
        while not 0<= jogador <= 10:
            print('Jogada inválida, tente novamente!')
            jogador = int(input('Me diga um número de 0 a 10: '))
print(f'Ha ha, eu acertei! Você disse {jogador} e eu disse {robo} também!')
