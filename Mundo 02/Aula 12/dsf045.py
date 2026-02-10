import emoji
from time import sleep
from random import choice
from playsound3 import playsound
sound = playsound("musica2.mp3", block=False)
print('\033[33m=-\33[m'*50)
print(emoji.emojize('Bem vindo ao pedra, papel, tesoura! Vamos batalhar!:smiling_face_with_sunglasses:'))
print('\33[34m=-\33[m'*50)
jogador = str(input('Você deseja jogar pedra, papel ou tesoura? ')).strip().lower()
escolhas = ['pedra', 'papel','tesoura']
robo = choice(escolhas)
sound2 = playsound('tambor.mp3',block=False)
print('Você e eu fizemos uma escolha!')
sleep(2)
print('Pedra..')
sleep(1)
print('Papel..')
sleep(1)
print('Tesouraaa..')
sleep(1)
sound2.stop()
if robo == jogador:
    print(f'Aaaa, \33[33mempatamos\33[m! Você escolheu \33[4m{jogador}\33[m e eu escolhi \33[4m{robo}\33[m!', emoji.emojize(':grinning_face_with_sweat:'))
#ganhar
elif (robo == 'pedra' and jogador == 'papel') or (robo == 'papel' and jogador == 'tesoura') or (robo == 'tesoura' and jogador == 'pedra'):
    print(f'\33[1mAH NÃO!\33[m Você \33[32mvenceu\33[m{emoji.emojize(':persevering_face:')}! Eu escolhi \33[4m{robo}\33[m e você escolheu \33[4m{jogador}\33[m! Na próxima vez irei lhe derrotar!')
    playsound('ganhar.mp3')
#perder
else:
    print(f'\33[7mMUAHAHAH!\33[m Você \33[31mperdeu\33[m{emoji.emojize(':relieved_face:')}! Eu escolhi \33[4m{robo}\33[m e você \33[4m{jogador}\33[m! Boa sorte na próxima vez... {emoji.emojize(':yawning_face:')}!')
    playsound('perder.mp3')
input('')
