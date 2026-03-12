from random import randint
a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)
tupla = (a,b,c,d,e)
print('Os números gerados aleatoriamente foram:')
for c in tupla:
    print(f'-{c}')
tupla = sorted(tupla)
print(f'O maior valor foi {tupla[4]}')
print(f'O menor valor foi {tupla[0]}')