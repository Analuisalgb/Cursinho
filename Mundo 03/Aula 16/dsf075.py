num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite mais um valor: '))
num4 = int(input('Digite o último valor: '))
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
print('foram pares!')
print('=-'*50)
