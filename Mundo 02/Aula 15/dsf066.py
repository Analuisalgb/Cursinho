cont = 0
soma = 0
num = 0
while True:
    num = int(input('Digite um número inteiro (0 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma de {cont} número(s) foi {soma}!')