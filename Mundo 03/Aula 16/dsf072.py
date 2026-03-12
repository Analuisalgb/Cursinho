numeros = ('zero', 'um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while not 0 <= num <= 20:
    print('Opção inválida! ')
    num = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[num]}')