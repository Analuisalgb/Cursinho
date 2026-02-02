print(f'{'Bem vindo ao desafio de número 23! Me diga um numero de 0 a 9999 e eu o separarei por suas casas!':=^100}')
num = int(input('Digite um número de 0 a 9999: '))
unidade = num % 10
dezena = (num % 100 - unidade) /10
centena = (num % 1000 - num % 100) /100
milhar = (num % 10000 - num % 1000) /1000
print(f'Unidade: {unidade} \n Dezena: {dezena} \n Centena: {centena} \n Milhar: {milhar}')


