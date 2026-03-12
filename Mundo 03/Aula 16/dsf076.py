produtos = ('Monitor', 560, 'RTX 5060ti', 2600, 'Suporte de monitor', 129.99, 'Livro', 59.97, 'Quadro', 680.34)
print('=-'*50)
print('Tabela de preços')
print('=-'*50)
for c in range(0,9,2):
    print(f'{produtos[c]:.<30} R$', end='')
    c += 1
    print(f'{produtos[c]: >10}')
print('=-'*50)
