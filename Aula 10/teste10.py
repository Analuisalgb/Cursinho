login = input('Digite um novo nome de usuário: ').strip()
senha = input('Digite uma nova senha: ').strip()
print('Conta criada!' )
verflogin = input('Digite o seu nome de usuário cadastrado: ')
verfsenha = input('Digite a sua senha: ')
if verflogin == login and verfsenha == senha:
    print('Bem vindo(a) {}! Cadastro concluído com sucesso!'.format(login))
else:
    print('Login ou senha inválidos!')