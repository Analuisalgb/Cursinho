print('{:=^100}'.format('Bem vindo ao desafio 11! Calcularei a quantidade de tinta necessária para pintar uma parede!'))
largura = float(input('Qual a largura da sua parede em metros? '))
altura = float(input('Qual a altura da sua parede em metros? '))
area = largura * altura
tinta = area / 2
print('A área da sua parede é: {} metros quadrados e você precisará de {} litros de tinta!'.format(area, tinta))