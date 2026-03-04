maiores = 0
homens = 0
mulheresNovas = 0
cont = 0
continuar = 'S'

while continuar == 'S':
    cont += 1
    idade = int(input(f'Qual é a idade da {cont}ª pessoa? '))
    sexo = str(input(f'Qual é o sexo da {cont}ª pessoa? [M/F] ')).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresNovas +=1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print(f'Das {cont} pessoas citadas, {maiores} tem mais 18 anos, {homens} são homens e {mulheresNovas} mulheres tem menos de 20 anos!')
