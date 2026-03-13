pessoas = []
dados = [[],[]]
continuar = 'S'
soma = 0
mostrar = 10
while continuar == 'S':
    dados[0].append(str(input('Nome: ')))
    dados[1].append(float(input('Nota 1: ')))
    dados[1].append(float(input('Nota 2: ')))
    pessoas.append(dados[:])
    dados = [[], []]
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        print('opção invalida! ')
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
print('=-'*50)
print('Num-  Nome-        Média')
print('-'*30)
for c in range(0,len(pessoas)):
    print(c+1, end ='     ')
    for d in range(len(pessoas[c])):
        if d == 0:
            print(f"{pessoas[c][0][0]:<20}",end='')
        else:
            print(f"{(pessoas[c][1][0] + pessoas[c][1][1]) / 2:>5}")
            break

print('-'*30)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (0 para interromper)'))
    if mostrar == 0:
        break
    print(f'As notas de {pessoas[mostrar-1][0][0]} são {pessoas[mostrar-1][1]}')
print('-'*30)
print('Encerrando programa...')