print('{:=^100}'.format('Bem vindo ao 09 desafio! Digite uma distância em metros, e eu converterei em km, cm e mm!'))
m = float(input('Digite o seu valor em metros: '))
km = m / 1000
cm = m * 100
mm = m * 1000
print('A sua distância em kilômetros é {}\nA sua distância em centímetros é {}\nA sua distância em milímetros é {}'.format(km, cm, mm))
