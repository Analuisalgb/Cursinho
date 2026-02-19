print('\33[34m=-\33[m'*50)
print('Me diga 6 números e eu lhe direi a soma! (Apenas dos pares...)')
print('\33[33m=-\33[m'*50)
s = 0
for i in range(0,7):
    num = int(input('Digite um número? '))
    if num % 2 == 0:
        s = s + num
print(f'A soma dos números pares enviados é: {s}')