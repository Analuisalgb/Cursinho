numeros = []
pares = []
impares = []
continuar = 'S'
while continuar == 'S':
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar not in 'SN':
        print('Opção inválida! Tente novamente.')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
for n in numeros:
    if n == 0:
        pares.append(n)
    elif n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)

print('Dos números digitados: ')
for n in numeros:
    print(f'{n}', end=' ')
print('')
print('Esses foram os números pares: ')
for p in pares:
    print(p, end=' ')
print('')
print('E esses foram os números impares: ')
for i in impares:
    print(i, end = ' ')
