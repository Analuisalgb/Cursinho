numeros =[[],[]]
for c in range(1,8):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f'Os valores pares digitados ( em ordem crescente ) foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados ( em ordem crescente ) foram: {sorted(numeros[1])}')