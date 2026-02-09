import random
print(f'{'Bem vindo ao desafio 28! Para ganhar o desafio, você tentará adivinhar o numéro que escolhi de 00 a 05!':=^100}')
numaleatorio = random.randint(0,5)
numescolhido = int(input('Digite um número de 0-5: '))
if numescolhido == numaleatorio:
    print('Parabéns você \033[32macertou\33[m! O número correto realmente era {}!'.format(numescolhido))
else:
    print(f'Você \033[31merrou!\033[m O número correto era \33[4;32m{numescolhido}\33[m')