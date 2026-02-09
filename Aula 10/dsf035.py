print(f'{'Bem vindo ao desafio 35! Me diga o comprimento de 3 retas e eu lhe direi se elas podem formar um triângulo!':=^100}')
reta1 = int(input('Qual o valor da primeira reta? '))
reta2 = int(input('Qual o valor da segunda reta? '))
reta3 = int(input('Qual o valor da terceira reta? '))
if reta1+reta2 > reta3 and reta1+reta3 > reta2 and reta2+reta3 > reta1:
    print(f'Com os valores de reta {reta1},{reta2} e {reta3} \33[32mé possível formar um triângulo\33[m!')
else:
    print(f'Com os valores {reta1}, {reta2} e {reta3} \33[31mé impossível formar um triângulo \33[34m:(\33[m')
