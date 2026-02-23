maior = 0
menor = 0
for p in range(1,6):
    peso = int(input(f'Digite o peso da {p} pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso foi o {maior} e o menor peso foi o {menor}!')