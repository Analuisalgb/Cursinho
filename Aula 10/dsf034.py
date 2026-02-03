print('{:=^100}'.format('Bem vindo ao desafio 34! Digite o seu salário e eu calcularei o seu aumento! '))
salario = float(input('Digite o seu salário: '))
if salario > 1250:
    novosalario = salario * 1.1
    print(f'O seu novo salário é {novosalario:.2f}!')
else:
    novosalario = salario * 1.15
    print(f'O seu novo salário é {novosalario:.2f} reais!')
