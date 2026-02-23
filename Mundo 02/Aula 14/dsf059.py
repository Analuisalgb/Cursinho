from time import sleep
continuar = True
num1 = 0
num2 = 0
while continuar == True:
    print('\33[34m=-\33[m'*50)
    operacao = int(input('''Qual operação deseja realizar?
        [1] Somar
        [2] Subtrair
        [3] Dividir
        [4] Multiplicar
        [5] Maior valor
        [6] Sair do programa
        '''))
    print('\33[33m=-\33[m' * 50)
    if operacao != 6:
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
        print('\33[34m=-\33[m' * 50)
        if operacao == 1:
            print(f'{num1} + {num2} = {num1 + num2}')
        if operacao == 2:
            print(f'{num1} - {num2} = {num1 - num2}')
        if operacao == 3:
            print(f'{num1} / {num2} = {num1 / num2}')
        if operacao == 4:
            print(f'{num1} x {num2} = {num1 * num2}')
        if operacao == 5:
            if num1 > num2:
                print(f'Entre os dois valores citados, o número {num1} é maior que o número {num2}!')
            elif num2 < num1:
                print(f'Entre os dois valores citados, o número {num2} é maior que o número {num2}!')
            else:
                print(f'Os valores {num1} e {num2} são iguais!')
        print('\33[33m=-\33[m' * 50)
    if operacao == 6:
        print('Encerrando...')
        continuar = False
    sleep(2)

