print('{:=^100}'.format('Bem vindo ao desafio 12! Diga o valor do produto e eu te direi o desconto :D'))
valor = float(input('Qual o valor do seu produto? '))
desconto = valor * 0.95
print('O produto de {:.2f}R$ fica por {:.2f}R$ com o desconto aplicado!'.format(valor, desconto))