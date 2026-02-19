import emoji
print(f'{'\033[32m=-\033[37m=-\033[m'*25}', emoji.emojize(':saluting_face:'))
print('Bem vindo ao desafio 39! Me diga sua idade e te informarei sobre o alistamento militar!')
print(f'{'\033[32m=-\033[37m=-\033[m'*25}', emoji.emojize(':saluting_face:'))
idade = int(input('Qual é a sua idade? '))
if idade == 18:
    print('Você está na idade \33[32mcorreta\33[m para o alistamento militar!')
elif idade < 18:
    tempf = 18 - idade
    print(f'Você \033[31mnão\033[m está na idade do alistamento militar! Restam \033[33m{tempf}\33[m ano(s) para o seu alistamento!')
else:
    tempf = idade - 18
    print(f'Seu alistamento está \33[33matrasado!\33[m Você deveria ter se alistado há \033[31m{tempf} ano(s)!\033[m')