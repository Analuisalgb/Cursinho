sexo = str(input('''Bem vindo ao nosso censo, poderia informar o seu sexo?'
      [M]- Masculino
      [F]- Feminino
       ''')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('''Opção inválida! Digite novamente:
                 [M] Masculino
                 [F] Feminino
                 ''')
if sexo == 'M':
    print('Sexo registrado com sucesso (Masculino). Obrigada pela ajuda!')
elif sexo == 'F':
    print('Sexo registrado com sucesso (Feminino). Obrigada pela ajuda!')
