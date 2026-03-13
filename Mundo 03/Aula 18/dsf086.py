matriz = [[],[],[]]
for a in range(0,3):
    for b in range(0,3):
        matriz[a].insert(b,int(input(f'Digite um valor para a posição [{a},{b}]: ')))
print('=-'*50)
for c in matriz:
    for p in c:
        print(f'[{p}]', end=' ')
    print('')
