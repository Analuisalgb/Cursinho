from time import sleep
print('\33[34m=-\33[m'*50)
print('Bem vindo ao desafio 61! Me diga o primeiro termo e a razão de uma P.A e eu lhe direi 10 termos!')
print('\33[33m=-\33[m'*50)
razao = int(input('Me diga a razão de sua P.A: '))
primeiroTermo = int(input('Me diga o primeiro termo de sua P.A: '))
cont = 1
parar = False
while cont <= 10:
    print(primeiroTermo + (cont - 1) * razao, end='')
    if cont != 10:
        print('->', end='')
    cont += 1
print('')
while parar == False:
    sleep(2)
    print('')
    mais = int(input('Deseja mostrar mais quantos termos? '))
    soma = mais + cont
    if mais == 0:
        print('Encerrando programa..')
        sleep(1)
        parar = True
    else:
        while cont <= soma :
            print(primeiroTermo + (cont - 1) * razao, end='')
            if cont != soma:
                print('->', end='')
            cont += 1
