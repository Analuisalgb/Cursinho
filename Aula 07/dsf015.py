print('{:=^100}'.format('Bem vindo ao desafio 15! Informe os valores a seguir e calcularei o valor do aluguel do carro'))
km = float(input('Quantos kilômetros foram rodados? '))
dias = int(input('Quantos dias o carro foi utilizado? '))
valort = 60 * dias + 0.15 * km

print('Por rodar {}km em {} dias o valor do seu aluguel ficou {:.2f}R$!'.format(km,dias,valort))