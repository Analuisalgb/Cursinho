print(f'\033[34m{'=-'*50}\033[m')
print('Bem vindo ao desafio 036! Eu irei calcular o valor e se você pode fazer um empréstimo!')
print(f'\033[33m{'=-'*50}\033[m')
vcasa = float(input('Qual o valor da casa em reais? '))
salario = float(input('Qual o valor do seu salário mensal? '))
anos = int(input('Em quantos anos deseja quitar seu empréstimo? '))
meses = anos * 12
prestacao = vcasa / meses
if prestacao > salario*0.3:
    print('\033[31mÉ impossível a realização desse empréstimo!\033[m')
else:
    print(f'Uma casa de {vcasa} reais quitada em {anos} anos ficará com uma prestação mensal de {prestacao:.2f} reais!')