print(f'{'Bem vindo ao desafio 32! Diga um ano e eu lhe direi se ele é bissexto!':=^100}')
ano = input('Digite um ano: ')
ano2 = int(ano)
if ano[2] != "0" and ano[3] != "0":
    if ano2 % 4 == 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto!')
else:
    if ano2 % 400 == 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto!')
