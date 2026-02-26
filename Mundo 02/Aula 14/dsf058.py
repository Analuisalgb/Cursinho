from random import randint
jogador = 20
robo = -1.2454687
cont = 0
while jogador != robo:
    robo = randint(0,10)
    jogador = int(input('Digite um número de 1 a 10: '))
    cont += 1
    if jogador != robo and 0 <= jogador <= 10:
        print(f'Ha! Você não acertou! Eu disse {robo} e você disse {jogador}. Tente novamente...')
    if not 0 <= jogador <= 10:
        print('Jogada inválida!')
        cont -= 1
print(f'Ah não, você acertou depois de {cont} tentativas! Você falou {jogador} e eu falei {robo}!')

#depois de analisar, vi que o código funciona mas pode ser limpo, a exemplo da definiç~çoa da variável do robo e do jogador antes, mas
#de resto ta topzera