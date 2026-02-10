print(f'\033[34m{'=-'*50}\033[m')
print(f'Bem vindo ao desafio 38! Me diga 2 números e eu irei comparar-los!')
print(f'\033[33m{'=-'*50}\033[m')
num1 = int(input('Digite o seu primeiro número inteiro: '))
num2 = int(input('Digite o seu segundo número inteiro: '))
if num1 > num2:
    print('O número {} é maior que o número {}!'.format(num1, num2))
elif num2 > num1:
    print(f'O número {num1} é maior que o número {num2}!')
else:
    print('Os dois valores são iguais!')