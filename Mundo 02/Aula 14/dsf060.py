print('\33[34m=-\33[m'*50)
print('Bem vindo ao desafio 60! Me diga um número e eu lhe direi seu fatorial!')
print('\33[33m=-\33[m'*50)
num = input('Digite um número inteiro e positivo: ')
while num.isdigit() == False:
    print('Número inválido! Tente novamente:')
    num = input('Digite um número inteiro e positivo: ')
num = int(num)
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