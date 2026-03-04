num = int(input('Digite um número: '))
while num > 0  :
    for c in range (1,11):
        print(f'{num} x {c} = {num*c}')
    c = 1
    num = int(input('Digite outro número: '))
print('Número inválido! Fim')
