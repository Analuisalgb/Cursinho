cont = 0
soma = 0
num= int(input('Digite um número qualquer: '))
while num != 999:
    num= int(input('Digite um número qualquer: '))
    cont +=1
    soma += num
print(f'Parando programa! Você digitou {cont} números, que juntos somam {soma} !')
