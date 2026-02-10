n = input('Digite algo: ')
#Como está definido como float ele vai printar o valor com o ponto, mesmo que não tenha antes
##Existe como converter valores strings em númerico após a variável, ´primeiro fazemos a
##chegagem para ver se é possível usando os comandos abaixo
print('Pode ser número?', n.isnumeric())
##para ver se pode ser letra
print('Pode ser letra?',n.isalpha())
print('Pode ser alfanumérico??',n.isalnum())
