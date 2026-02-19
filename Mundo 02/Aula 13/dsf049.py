print(f'{'\33[34m=-\33[m'*50}')
print('Bem vindo ao desafio 49! Me diga um número e eu lhe direi sua tabuada!')
print(f'{'\33[33m=-\33[m'*50}')
num = int(input('Digite um número: '))
vezes = int(input('Quantas linhas deve ter sua tabuada? '))
print('\33[33m=-\33[m'*30)
for c in range (0, vezes):
    print(f'{num} x {c} = {num*c}')
print('\33[34m=-\33[m'*30)