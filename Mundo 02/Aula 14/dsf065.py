parar = False
num = int(input('Digite o número: '))
maiornum = num
menornum = num
soma = num
cont = 1
print(soma)
print(cont)
while parar == False:
    confirmar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if confirmar == 'N':
        soma += num
        cont += 1
        break
    elif confirmar != 'S' and confirmar != 'N':
        cont -= 1
        print('Opção inválida! ')
    num = int(input('Digite o número: '))
    if num > maiornum:
        maiornum = num
    elif num < menornum:
        menornum = num
    soma += num
    cont += 1
    print(soma)
    print(cont)
media = soma / cont
print(f'Dentre os {cont} valore(s) citado(s), a média foi {media:.2f}, o maior número foi {maiornum} e o menor número foi {menornum}!')
