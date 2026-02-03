import math
print(f'{'Bem vindo ao desafio 33! Me diga 3 números e eu lhe direi qual é o maior!':=^100}')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
    print(f'O maior número é o {num1}!')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é o {num2}!')
elif num3 > num1 and num3 > num2:
    print(f'O maior número é o {num3}!')
else:
    print(f'Não é possível determinar o maior número já que há dois ou mais valores iguais!')
if num1 < num2 and num1 < num3:
    print(f'O menor número é o {num1}!')
elif num2 < num1 and num2 < num3:
    print(f'O menor número é o {num2}!')
elif num3 < num1 and num3 < num2:
    print(f'O menor número é o {num3}!')
else:
    print('Não é possível determinar o menor número já que há dois ou mais valores iguais!')