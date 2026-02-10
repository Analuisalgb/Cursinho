import random
from time import sleep
start = input(f'{'Aperte enter para rolar o seu d20!':=^100}')
print('.',end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print(f'O rolamento do seu dado foi {random.randint(1, 20)}!')
