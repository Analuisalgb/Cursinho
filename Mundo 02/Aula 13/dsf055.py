pesoi = int(input('Digite o seu peso: '))
pesoo = int(input('Digite o seu peso: '))
if pesoi>pesoo:
    pesoma = pesoi
    pesome = pesoo
    pesoig = 0
if pesoi<pesoo:
    pesome = pesoi
    pesoma = pesoo
    pesoig = 0
else:
    pesoig = pesoi = pesoo
    pesoma = pesoig
    pesome = pesoig
    quantpig =+ 2
for c in range (0,3):
    pesoo = int(input('Digite o seu peso: '))
    if pesoo > pesoma:
        pesoma = pesoo
    elif pesoo < pesome:
        pesome = pesoo
    elif pesoo == pesoig or pesoo == pesoma or pesoo == pesome:
        pesoig = pesoi = pesoo
        quantpig = + 1
    pesoi = pesoo
print(f'O menor peso é: {pesome}!')
print(f'O maior peso é: {pesoma}!')
if pesoig != 0:
    print(f'A {quantpig} iguais pesos de valor {pesoig}!')

