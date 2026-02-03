import random
print(f'{'Bem vindo ao desafio 28! Para ganhar o desafio, você tentará adivinhar o numéro que escolhi de 00 a 05!':=^100}')
numaleatorio = random.randint(0,5)
numescolhido = int(input('Digite um número de 0-5: '))
if numescolhido == numaleatorio:
    print('Parabéns você acertou! O número correto realmente era {}!'.format(numescolhido))
else:
    print('Você errou! O número correto era {}'.format(numaleatorio))