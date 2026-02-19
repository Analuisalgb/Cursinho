print('\33[33m=-\33[m'*50)
print('Bem vindo à sua própria P.A.! Me diga sua razão e o termo inicial e eu calcularei os 10 primeiros termos!')
print('\33[34m=-\33[m'*50)
razao = int(input('Qual a razão da sua P.A. ? '))
termoInicial = int(input('Qual é o termo inicial da sua P.A. ? '))
for c in range(1,11):
    print(termoInicial + razao * (c-1))
