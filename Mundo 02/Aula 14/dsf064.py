cont = 0
soma = 0
num= int(input('Digite um número qualquer: '))
while num != 999:
    cont +=1
    soma += num
    num = int(input('Digite um número qualquer: '))
print(f'Parando programa! Você digitou {cont} número(s), que juntos somam {soma} !')
