print(f'{'\33[34m=-\33[m'*50}')
print('Bem vindo ao desafio 48! Irei te dizer a somatodos os números ímpares e múltiplos de 3 entre 1 e 500!')
print(f'{'\33[33m=-\33[m'*50}')
s = 0
for c in range(0,501,3):
    if c % 2 != 0:
        s = s+c
print(f'A soma de todos os números impares e múltiplos de 3 entre 1 e 500 é: {s}!')