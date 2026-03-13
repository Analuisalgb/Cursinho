matriz = [[],[],[]]
somapar = 0
somact = 0

for a in range(0,3):
    for b in range(0,3):
        matriz[a].insert(b,int(input(f'Digite um valor para a posição [{a},{b}]: ')))

print('=-'*50)

for c in matriz:
    for p in c:
        print(f'[{p}]', end=' ')
    print('')

for c in matriz:
    for p in c:
        if p % 2 == 0:
            somapar += p
for c in range(0,3):
    somact += matriz[c][2]

print(f'A soma de todos os elementos pares da matriz é: {somapar}')
print(f'A soma de todos os elementos da coluna tres é: {somact}')
print(f'O maior elemento da segunda linha é: {max(matriz[1])}')
