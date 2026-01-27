import random
print(f'{'Bem vindo ao desafio 20! Diga o nome de quatro alunos, sortearei a ordem de apresentação de cada um!':=^100}')
nome1 = str(input('Qual o nome do primeiro aluno? '))
nome2 = str(input('Qual o nome do segundo aluno? '))
nome3 = str(input('Qual o nome do terceiro aluno? '))
nome4 = str(input('Qual o nome do quarto aluno? '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(f'A ordem dos alunos, respectivamente é {random.sample(lista, len(lista))}!')
print(f'A ordem dos alunos, respectivamente é {lista}!')