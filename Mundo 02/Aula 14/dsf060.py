print('\33[34m=-\33[m'*50)
print('Bem vindo ao desafio 60! Me diga um número e eu lhe direi seu fatorial!')
print('\33[33m=-\33[m'*50)
num = 0
while True:
    num = int(input('Digite um número inteiro e positivo: '))
    if num == float or num < 0:
        print('Número inválido!')
    else:
        break
if num != 0:
    print(f'{num}! = {num} x ', end='')
    fatorial = num
    while num > 1:
        num -= 1
        fatorial *= num
        print(num, end='')
        if num != 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
    print(fatorial)
else:
    print(f'{num}! = 1')