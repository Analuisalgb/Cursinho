soma = 0
idadema = 0
idademe = 0
for c in range (1,5):
    nome = str(input('Qual o seu nome? ')).strip()
    idade = int(input('Qual a sua idade? '))
    sexo = int(input('''Qual o seu sexo?
      [1]- Masculino
      [2]- Feminino
         '''))
    soma = soma + idade
    media = soma / c
    if sexo == 2 and idade < 20:
        mulhermenor =+ 1
    if sexo == 1:
        if idade > idadema:
            idadema = idade
            NomeHMmaior = nome
print('A media das idades é: {}'.format(media))
print(f'Há {mulhermenor} mulhere(s) com menos de 20 anos! ')
print(f'Nossa {NomeHMmaior}! Você é o homem mais velho, com {idadema} anos!')
