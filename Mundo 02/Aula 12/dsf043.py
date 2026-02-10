print(f'{'=-'*50}')
print('Bem vindo ao desafio 43! Me diga seu peso e sua altura e eu calcularei seus status baseado no IMC!!')
print(f'{'=-'*50}')
peso = int(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Segundo o IMC, você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Segundo o IMC, você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Segundo o IMC, você está acima do peso!')
elif imc >= 30 and imc < 40:
    print('Segundo o IMC, você está com obesidade!')
else:
    print('Segundo o IMC, você está com obesidade mórbida!')