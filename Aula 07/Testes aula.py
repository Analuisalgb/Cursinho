nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:^30}!'.format(nome))
print('Prazer em te conhecer {:<30}!'.format(nome))
print('Prazer em te conhecer {:>30}!'.format(nome))
print('Prazer em te conhecer {:=^30}!'.format(nome))
#ao botar o == ele completa o espaço com iguais

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
e = n1**n2
print(' A soma é {} \n A multiplicação é {} \n A divisão é {:.4f} \n A exponenciação é {}'.format(s, m, d, e))