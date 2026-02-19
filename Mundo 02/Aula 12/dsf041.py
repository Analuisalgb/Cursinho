print(f'{'\33[34m=-\33[m'*50}')
print('Bem vindo ao desafio 41! Me diga sua idade e eu lhe direi a que categoria esportiva você está incluído!')
print(f'{'\33[33m=-\33[m'*50}')
idade = int(input('Qual a sua idade? '))
if idade <= 9:
    print('Você pertence a categoria Mirim!')
elif idade <= 14:
    print('Você pertence a categoria Infantil!')
elif idade <= 19:
    print('Você pertence a categoria Junior!')
elif idade <= 25:
    print('Você pertence a categoria Sênior!')
else:
    print('Você pertence a categoria Master!')