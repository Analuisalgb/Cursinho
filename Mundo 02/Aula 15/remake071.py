saque = int(input('Qual o valor que deseja sacar? R$ '))
resto = saque
notas = [50,20,10,1]
quantnotas = [0,0,0,0]
cont = 0

print(f'Ao total, para sacar R${saque:.2f} se usarão:')

while cont <= 3:
    if resto != 0 and resto // notas[cont] != 0:
        quantnotas[cont] = resto // notas[cont]
        resto = resto - quantnotas[cont] * notas[cont]

    if quantnotas[cont] > 0:
        print(f'- {quantnotas[cont]} nota(s) de {notas[cont]}')
    cont += 1