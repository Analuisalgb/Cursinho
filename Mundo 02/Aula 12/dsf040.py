print(f'{'\33[34m=-\33[m'*20}')
print('Bem vindo ao desafio 40! Me diga a média das sua escola e suas duas notas e lhe direi se você passou!')
print(f'{'\33[33m=-\33[m'*20}')
media = int(input('Qual a média da sua escola? '))
nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))
mediaIndividual = (nota1 + nota2) / 2
if mediaIndividual >= media:
    print('Parabéns! Você foi \33[32maprovado\33[m!')
elif mediaIndividual < media and mediaIndividual >= media-2:
    print('Você está em \033[33mrecuperação!\033[m')
else:
    print('Você \033[31mreprovou!\033[m')
