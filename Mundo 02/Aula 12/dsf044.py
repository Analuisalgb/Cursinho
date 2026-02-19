from webbrowser import Elinks

print('{}'.format('\033[33m=-\33[m'*50))
print(f'Bem vindo ao desafio 44! Me diga o preço da compra e o metódo de pagamento e eu lhe direi o preço final!')
print(f'{'\33[34m=-\33[m'*50}')
preco = float(input('Qual o valor do seu pagamento? '))
print('=-' * 20)
metodo = str(input('Qual o seu método de pagamento? \n'
                   '[1] À vista dinheiro/cheque \n'
                   '[2] À vista no cartão (Débito) \n'
                   '[3] Em até 2x no cartão (Crédito)\n'
                   '[4] 3x ou mais no cartão (Crédito)\n'
                   ': ')).strip()
print('=-'*20)
if metodo == "1":
    valor = preco * 0.9
    print(f'Pagamento à vista selecionado!\nO valor final do produto de preço {preco} ficará por {valor}R$!')
elif metodo == "2":
    valor = preco * 0.95
    print(f'Pagamento pelo cartão de débito selecionado!\nO valor final do produto de preço {preco} ficará por {valor}R$!')
elif metodo == '3':
    valor = preco
    print(f'Pagamento pelo cartão de crédito em até 2 parcelas selecionado!\nO valor final do produto de preço {preco} ficará por {valor}R$!')
elif metodo == '4':
    valor = preco * 1.2
    print(f'Pagamento pelo cartão de crédito em mais de 2 parcelas selecionado!\nO valor final do produto de preço {preco} ficará por {valor}R$!')
else:
    print('\33[31mMétodo de pagamento selecionado é inexistente!\33[m')
print('=-' * 20)
