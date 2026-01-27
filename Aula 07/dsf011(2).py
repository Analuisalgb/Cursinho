print('{:=^100}'.format('Bem vindo ao desafio 11! Calcularei a quantidade de tinta necessária para pintar uma parede!'))
cobertura = float(input('Quantos metros quadrados a sua tinta rende por litro? '))
largura = float(input('Qual a largura da sua parede em metros? '))
altura = float(input('Qual a altura da sua parede em metros? '))
area = largura * altura
tinta = area / cobertura
print('A área da sua parede é: {} metros quadrados e você precisará de {} litros de tinta!'.format(area, tinta))