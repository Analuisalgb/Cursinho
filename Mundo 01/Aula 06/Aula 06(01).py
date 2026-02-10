nome=input('Qual o seu nome? ')
n1=int(input('Digite seu primeiro número: '))
n2=int(input('Digite seu segundo número: '))
s= n1+n2 #não precisa do parêntese
print('A soma foi:',s,'!')
#o print pode ser usado como
print('A soma foi: {}!' .format(s))
print(nome,'a soma entre',n1,'e',n2,'é:',s,'!')
#ou pode ser usar
print('{} a soma entre {} e {} é {}!' .format(nome,n1, n2, s))

#Para descobrir como o python está classificando uma variável podemos usar
print('a classe do primeiro número é',type(n1))
print('a classe do nome é',type(nome))
