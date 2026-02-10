import math
print(f'{'Bem vindo ao desafio 17! Me diga os dois catetos e eu te direi a hipotenusa':=^100}')
cateto1 = int(input('Qual o valor do seu primeiro cateto? '))
cateto2 = int(input('Qual o valor do seu segundo cateteto? '))
hipotenusa = math.hypot(cateto1, cateto2)
hipotenusa2 = math.sqrt(cateto1**2 + cateto2**2)
#hipotenusa = (cateto1**2 + cateto2**2) ** (1/2)
print(f'O valor da sua hipotenusa com os catetos {cateto1} e {cateto2} é {hipotenusa}')
print('O valor da sua hipotenusa com os catetos {} e {} é {}'.format(cateto1, cateto2, hipotenusa2))
