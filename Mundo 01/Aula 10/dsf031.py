print('{:=^100}'.format('Bem vindo ao desafio 31! Eu irei calcular sua viagem baseada na quilometragem!'))
km = int(input('Quantos quilômetros você viajará? '))
if km <= 200:
    preco = km * 0.5
    print(f'O preço da sua passagem ficou por \33[32m{preco} reais\33[m!')
else:
    preco = km * 0.45
    print(f'O preço da sua passagem ficou por \33[32m{preco} reais\33[m!')