numeros = []
continuar = 'S'
contador = 0
while continuar == 'S':
    numeros.append(int(input('Digite um valor: ')))
    contador += 1
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida! ')
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

print(f'Ao todo, {contador} valores foram digitados!')
print(f'Essa é a ordem dos seus números em ordem decrescente:')
numeros = sorted(numeros, reverse=True)
for n in numeros:
    print(f'{n} -> ', end = '')
if 5 in numeros:
    print(f' O número 5 apareceu na lista! ({numeros.count(5)} vezes) ')
else:
    print('O número 5 não apareceu na lista!')
