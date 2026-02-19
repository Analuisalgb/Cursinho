from playsound3 import  playsound
from time import sleep
from emoji import emojize
print(f'{'\33[31m=\33[35m-\33[m'*50}')
print('Os fogos vão começar!')
print(f'{'\33[31m=\33[35m-\33[m'*50}')
sleep(1)
for c in range(10,0, -1):
    print(f'{c}!')
    sleep(1)
playsound('fogos.mp3', block=False)
print(emojize(':fireworks:'),emojize(':sparkler:'))
input('')