print('{:=^100}'.format('Bem vindo ao desafio 29! Eu calculo suas mutas baseado na sua velocidade!'))
velocidade = int(input('Qual o valor da sua velocidade na via? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\33[31mVocê ultrapassou o limite de 80km/h!\33[m Sua multa ficou de {multa} reais!')
else:
    print('\33[32mMuito bem, sua velocidade está adequada à via!\33[m')
