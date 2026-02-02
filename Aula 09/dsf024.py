print(f'{'Bem vindo ao desafio 24! Me diga um nome de uma cidade e eu lhe direi se ela começa, ou não,com santo!':=^100}')
cidade = str(input('Qual o nome da sua cidade? ')).strip()
cidade = cidade.capitalize()
if cidade.find('Santo') == -1:
    print('A sua cidade não começa com Santo!')
else:
    print('A sua cidade começa com Santo!')