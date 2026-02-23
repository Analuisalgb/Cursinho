maiores = 0
menores = 0
for c in range(0,7):
    idade = int(input('Digite a sua idade: '))
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print(f'Ao todo, das idades fornecidas {maiores} pessoa(s) são maiores de idade e {menores} pessoa(s) são menores de idade!')
