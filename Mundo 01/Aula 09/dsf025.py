print(f'{'Bem vindo ao desafio 25! Me diga seu nome completo e eu direi se ele tem silva ou não!':=^100}')
nome = str(input('Qual o seu nome? '))
nome = nome.lower()
if nome.find('silva') == -1:
    print('Seu nome não tem Silva.')
else:
    print('Seu nome tem Silva!')