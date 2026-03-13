dados = []
pessoas = []
continuar = 'S'
maiorpeso = menorpeso = contador = 0
nomemaiorpeso = []
nomemenorpeso = []

while continuar == 'S':
    contador +=1
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        print('opção inválida, tente novamente.')
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    pessoas.append(dados[:])
    if contador == 1:
        maiorpeso = menorpeso = dados[1]
        nomemaiorpeso.append(dados[0])
        nomemenorpeso.append(dados[0])
    elif dados[1] > maiorpeso:
        maiorpeso = dados[1]
        nomemaiorpeso.clear()
        nomemaiorpeso.append(dados[0])
    elif dados[1] < menorpeso:
        menorpeso = dados[1]
        nomemenorpeso.clear()
        nomemenorpeso.append(dados[0])
    elif dados[1] == menorpeso:
        nomemenorpeso.append(dados[0])
    elif dados[1] == maiorpeso:
        nomemaiorpeso.append(dados[0])
    dados.clear()

print(f'Você cadastrou {contador} pessoas.')
print(f'O maior peso foi de {maiorpeso}KG. Peso de {nomemaiorpeso}')
print(f'O menor peso foi de {menorpeso}KG. Peso de {nomemenorpeso}')
