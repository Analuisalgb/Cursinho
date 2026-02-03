print('{:=^100}'.format('Bem vindo ao desafio 29! Eu calculo suas mutas baseado na sua velocidade!'))
velocidade = int(input('Qual o valor da sua velocidade na via? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de 80km/h! Sua multa ficou de {multa} reais!')
else:
    print('Muito bem, sua velocidade está adequada à via!')
