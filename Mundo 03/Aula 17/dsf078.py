valores = []
valoresori = valores[:]
contwhile = 1
for c in range(1,6):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
print('Você digitou os valores:', end=' ')
for c in valores:
    print(c, end=' ')
print('')
print(f'O maior valor digitado foi: {max(valores)} na posição {valores.index(max(valores)) + 1}', end =' ')
if valores.count(max(valores)) > 1:
    while valores.count(max(valores)) > 1:
        contwhile += 1
        valores.remove(max(valores))
        print(f'e {valores.index(max(valores)) + contwhile}', end=' ')
    print('')
print(f'E o menor valor digitado foi: {min(valores)} na posição {valores.index(min(valores)) + 1}', end=' ')
if valores.count(min(valores)) > 1:
    while valores.count(min(valores)) > 1:
        contwhile += 1
        valores.remove(min(valores))
        print(f'e {valores.index(min(valores)) + contwhile}', end=' ')
    print('')