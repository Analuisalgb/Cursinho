num = int(input('Digite o 1 valor: '))
lista = []
lista.append(num)
cont = 0

for c in range(2,6):
    num = int(input(f'Digite o {c} valor: '))
    for t in range(0,len(lista)):
        if num <= lista[t]:
            if t == 0:
                lista.insert(0,num)
            else:
                lista.insert(t, num)
            break
        elif t != 0 and t == len(lista) - 1:
            lista.append(num)
        elif num > lista[t] and t == len(lista) -1:
            lista.append(num)

print('Os números em ordem foram: ')
for c in lista:
    print(f'- {c}')