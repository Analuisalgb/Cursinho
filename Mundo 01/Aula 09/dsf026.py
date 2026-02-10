print(f'{'Bem vindo ao desafio 26! Me diga uma frase aleatória e eu te direi algumas informações!':=^100}')
frase = str(input('Digite uma frase: ')).strip().lower()
print(f'Na sua frase, a letra A aparece {frase.count('a')} vezes, aparecendo na primeira vez na posição {frase.find('a') + 1} e na ultima vez na posição {frase.rfind('a') + 1}')

