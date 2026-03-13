matriz = [[],[],[]]
for x in range(0,3):
    matriz[0].insert(x,int(input(f'Digite um valor para a posição [0,{x}]: ')))
for y in range(0,3):
    matriz[1].insert(y,int(input(f'Digite um valor para a posição [1,{y}]: ')))
for z in range(0, 3):
    matriz[2].insert(z, int(input(f'Digite um valor para a posição [2,{z}]: ')))
print('=-'*50)
for a in range(0,3):
    for b in range(0,3):
        matriz[a].insert(b,int(input(f'Digite um valor para a posição [{a},{b}]: ')))