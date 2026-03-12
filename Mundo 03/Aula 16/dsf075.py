num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite mais um valor: '))
num4 = int(input('Digite o último valor: '))
#valores = tuple(int(input('Digite valores '))for c in range(1, 5))
#valores = int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')))
par = 0
tupla = (num1, num2, num3, num4)
print('=-'*50)
print(f'O valor 9 apareceu {tupla.count(9)} vezes!')
if 3 in tupla:
    print(f'O primeiro valor 3 apareceu na tupla na posição {tupla.index(3) +1}')
print('Os números:')
for c in tupla:
    if c % 2 == 0:
        print(f'-{c}')
        par += 1
print(f'foram pares! ({par} números!)')
print('=-'*50)
