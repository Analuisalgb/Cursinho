print(f'{'\33[33m=-\33[m'*50}')
print('Bem vindo ao desafio 42! Me diga o valores de 3 retas e eu lhe direi se eles formam um triângulo e de que tipo formam!')
print(f'{'\33[34m=-\33[m'*50}')
reta1 = int(input('Digite o valor da primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    if reta1 == reta2 == reta3:
        print(f'As retas {reta1}, {reta2} e {reta3} formam um triângulo que é equilâtero!')
    elif reta1**2 == reta2**2 + reta3**2 or reta2**2 == reta1**2 + reta3**2 or reta3**2 == reta1**2 + reta2**2:
        print(f'As retas {reta1}, {reta2} e {reta3} formam um triângulo que é retângulo!')
    elif reta1**2 > reta2**2 + reta3**2 or reta2**2 > reta1**2 + reta3**2 or reta3**2 > reta1**2 + reta2**2:
        print(f'As retas {reta1}, {reta2} e {reta3} formam um triângulo que é obtusângulo!')
    elif reta1**2 < reta2**2 + reta3**2 or reta2**2 < reta1**2 + reta3**2 or reta3**2 < reta1**2 + reta2**2:
        print(f'As retas {reta1}, {reta2} e {reta3} formam um triângulo que é acutângulo!')
else:
    print(f'As retas {reta1}, {reta2} e {reta3} não formam um triângulo!')