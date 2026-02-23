print('\33[34m=-\33[m'*50)
print('Bem vindo ao desafio 63! Me diga um número e a quantidade de elementos e eu montarei uma sequência de Fibonacci!')
print('\33[33m=-\33[m'*50)
numero = int(input('Digite o numero inicial da sequência: '))
elementos = int(input('Digite a quantidade de elementos da sequência: '))
numant = 0
numnovo = numero
while elementos > 0:
    print(numnovo, end='')
    if elementos == 1:
        print('')
    else:
        print(' -> ', end='')
    numnovo = numero + numant
    numant = numero
    numero = numnovo
    elementos -=1