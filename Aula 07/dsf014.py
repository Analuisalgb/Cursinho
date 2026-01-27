print('{:=^100}'.format('Bem vindo ao desafio 14! Me diga uma temperatura em Celsius e converterei para Fahrenheit e Kelvin!'))
celsius = float(input('Qual a temperatura em Celsius? '))
farenheit = (celsius * 1.8) + 32
kelvin = celsius + 273
print('Uma temperatura de {}C é igual a {}F ou {}K'.format(celsius, farenheit, kelvin))
