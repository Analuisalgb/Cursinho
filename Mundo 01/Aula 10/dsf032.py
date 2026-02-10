print(f'\33[4;44m{'Bem vindo ao desafio 32! Diga um ano e eu lhe direi se ele é bissexto!':=^100}\33[m')
ano = input('Digite um ano: ')
ano2 = int(ano)
if ano[2] != "0" and ano[3] != "0":
    if ano2 % 4 == 0:
        print(f'O ano {ano} \33[32mé bissexto\33[m!')
    else:
        print(f'O ano {ano} \33[31mnão é bissexto\33[m!')
else:
    if ano2 % 400 == 0:
        print(f'O ano {ano} \33[32mé bissexto!\33[m')
    else:
        print(f'O ano {ano} \33[31mnão é bissexto\33[m!')
