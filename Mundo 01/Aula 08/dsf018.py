import math
print(f'{'Bem vindo ao desafio 18! Me diga um ângulo e eu lhe direi o seu cosseno, o seu seno e sua tangente!':=^100}')
angg = float(input('Qual o valor do seu angulo em graus? '))
angr = 0.0174533*angg
#existe uma função para converter para radianos math.radians(x)
print(f'O angulo de {angg} graus apresenta como cosseno {math.cos(angr):.4f}, como seno {math.sin(angr):.4f} e como tangente {math.tan(angr):.4f}!')