palavras = ('oi', 'parabens', 'heron', 'aniversario', 'bolo', 'alegria', 'pc', 'chega')
for c in range(0,len(palavras)):
    print(f'A palavra {palavras[c]} tem as vogais:')
    if palavras[c].count('a') != 0:
            print('A', end=' ')
    if palavras[c].count('e') != 0:
            print('E', end=' ')
    if palavras[c].count('i') != 0:
            print('I', end=' ')
    if palavras[c].count('o') != 0:
            print('O', end=' ')
    if palavras[c].count('u') != 0:
            print('U', end=' ')
    print('')