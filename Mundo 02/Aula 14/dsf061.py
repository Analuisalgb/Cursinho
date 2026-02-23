print('\33[34m=-\33[m'*50)
print('Bem vindo ao desafio 61! Me diga o primeiro termo e a razão de uma P.A e eu lhe direi 10 termos!')
print('\33[33m=-\33[m'*50)
razao = int(input('Me diga a razão de sua P.A: '))
primeiroTermo = int(input('Me diga o primeiro termo de sua P.A: '))
cont = 1
while cont <= 10:
    print(primeiroTermo + (cont - 1) * razao, end='')
    if cont != 10:
        print('->', end='')
    cont += 1
