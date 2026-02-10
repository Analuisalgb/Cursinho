print(f'\33[4;39;45m{'Bem vindo ao desafio 30! Me diga um número e eu lhe direi se ele é par!':=^100}\33[m')
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número {num} é \33[33mpar\33[m!')
else:
    print(f'O número {num} é \33[34mímpar!\33[m')
