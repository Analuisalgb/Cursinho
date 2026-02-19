num = int(input('Digite um número inteiro: '))
p = False
for c in range(2,num+1):
    if p == False:
        if num == 2:
            print('Esse número é primo!')
            p = True
        elif c != num and num % c == 0:
            print('Esse número não é primo!')
            p = True
        elif num == c:
            print('Esse número é primo!')
            p = True
