continuar = 'S'
num = []
numver = 0
while continuar == 'S':
    numver = int(input('Digite um valor: '))
    if numver in num:
        print('Valor já foi digitado, tente novamente!')
        continue
    else:
        num.append(numver)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida, tente novamente!')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

print('=-'*50)
print('Os valores digitados em ordem foram: ', end=' ')
num = sorted(num)
for c in num:
    print(f'->{c}', end =' ')



