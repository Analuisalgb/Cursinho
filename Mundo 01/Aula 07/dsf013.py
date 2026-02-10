print('{:=^100}'.format('Bem vindo ao desafio 13! Me diga seu salário e eu lhe informarei o novo valor com o aumento!'))
salario = float(input('Qual é o seu salário mensal? '))
saumento = salario * 1.15
diferenca = saumento - salario
print('O seu salário de {} com os aumentos ficou de {} (um incremento de {})!'.format(salario, saumento, diferenca))