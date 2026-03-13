lista = []
num = int(input(f'Digite o 1 valor: '))
lista.append(num)
cont = 2

while cont <=5:
    num = int(input(f'Digite o {cont} valor: '))
    if num in lista:
        lista.insert(num, lista.index(num)+1)
    else:
        for c in range (0,cont):
            if num > lista[c]:
                if num in lista:
                    lista.remove(num)
                lista.insert(c+1,num)
            elif num < lista[c]:
                if c == 0:
                    lista.insert(0,num)
                else:
                    if num in lista:
                        lista.remove(num)
                    lista.insert(c-1,num)
    print(lista)
    cont +=1
print('Os números, em ordem são:')
for c in lista:
    print(f'-{c}')