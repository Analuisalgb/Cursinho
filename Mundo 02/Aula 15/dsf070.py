precop = totalpreco = maisquemil = maisbarato = 0
quant = 1
nomemaisbarato = nomep = ''
continuar = 'S'

while continuar == 'S':
    print('=-'*50)
    nomep = str(input(f'Qual é o nome do seu {quant}ᵒ produto? '))
    precop = float(input(f'Qual é o valor do seu {quant}ᵒ produto? '))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('=-'*50)
    if quant == 1 or precop <maisbarato:
        maisbarato = precop
        nomemaisbarato = nomep
    if continuar != 'S' and continuar != 'N':
        print('Opção inválida! Tente novamente: ')
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    quant += 1
    totalpreco += precop
    if precop > 1000:
        maisquemil += 1

print(f'O total da compra foi de R${totalpreco:.2f}. \n{maisquemil} produtos custaram mais que mil reais!\n{nomemaisbarato.capitalize()} foi o produto mais barato (R${maisbarato})!')