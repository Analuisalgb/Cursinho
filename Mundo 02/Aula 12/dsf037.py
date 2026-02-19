print(f'\033[34m{'=-'*50}\033[m')
print('Bem vindo ao desafio 37! Me diga um número e uma base e eu o converterei!')
print(f'\033[33m{'=-'*50}\033[m')
numero = int(input('Me diga um número inteiro: '))
base = str(input('''Para qual base você deseja converter?
[B] para binário
[H] para hexadecimal
[O] para octadecimal:
''')).upper().strip()
if base == 'B':
    print(f'O seu número em binário é: {bin(numero)[2:]}')
elif base == 'H':
    print(f'O seu número em hexadecimal é: {hex(numero)[2:]}')
elif base == 'O':
    print(f'O seu número em octadecimal é: {oct(numero)[2:]}')
else:
    print('\033[31mBase inválida!\033[m')
