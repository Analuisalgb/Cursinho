expressao = str(input('Digite a sua expressão: ')).strip()
esq = expressao.count('(')
dir = expressao.count(')')
if esq == dir:
    print('Sua expressão está certa, operação válida!')
else:
    print('Sua expressão está incorreta, operação inválida!')