from random import choice
print(f'{'Bem vindo ao desafio 19! Me diga o nome das pessoas e eu escolherei uma para ler a questão!':=^100}')
nome1 = str(input('Qual o nome do primeiro aluno? '))
nome2 = str(input('Qual o nome do segundo aluno? '))
nome3 = str(input('Qual o nome do terceiro aluno? '))
nome4 = str(input('Qual o nome do quarto aluno? '))
lista = [nome1, nome2, nome3, nome4]
print(f'O aluno escolhido para ler a questão foi {choice(lista)}')