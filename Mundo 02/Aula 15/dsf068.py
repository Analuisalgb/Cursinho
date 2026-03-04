from random import randint
from time import sleep
cont = 0
robo = randint(0,10)
print('Vamos brincar de par ou impar! ')
while True:
    opcao = str(input('Você quer par ou impar?[P/I] ')).upper().strip()[0]
    while opcao not in 'PI':
        opcao = str(input('Você quer par ou impar?[P/I] ')).upper().strip()[0]
    jogador = int(input('Digite o número que você quer jogar: '))
    print('Vamos arrastar! ')
    sleep(1)
    print(f'Você jogou {jogador} e eu joguei {robo}! \nA soma de nossas jogadas deu {jogador + robo}, então..',end='')
    if opcao == 'P' and (jogador + robo) % 2 == 0:
        print(' como você escolheu par você ganhou! \nVamos para mais uma rodada...')
        cont +=1
    elif opcao == 'I' and (jogador + robo) % 2 != 0:
        print(' como você escolheu impar você ganhou! \nVamos para mais uma rodada...')
        cont += 1
    else:
        cont += 1
        break
if opcao == 'P':
    print(f' a soma de nossos valores foi ímpar! Hahah eu ganhei depois de {cont} rodadada(s)!')
if opcao == 'I':
    print(f' a soma de nossos valores foi par! Hahah eu ganhei depois de {cont} rodadada(s)!')