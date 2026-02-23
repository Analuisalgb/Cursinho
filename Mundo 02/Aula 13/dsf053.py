frase = str(input('Digite uma frase: ')).strip().upper().split()
frase = ''.join(frase)
fraserev = (frase[len(frase): : -1])
print(f'O inverso de {frase} é: {fraserev}, logo:')
if fraserev == frase:
    print('Sua frase é um palíndromo! ')
else:
    print('Sua frase NÃO é um palíndromo! :(')