classificacao = ('Palmeiras','São Paulo','Corinthians','Bahia','Fluminense','Athletico Paranaense','Bragantino','Grêmio','Mirassol','Chapecoense','Santos','Flamengo','Coritiba','Botafogo','EC vitória','Remo','Atlético MG','Internacional','Cruzeiro','Vasco da gama')
print('=-'*50)
print('Os 5 primeiros colocados são:')
for c in range(1,6):
    print(f'{c}-{classificacao[c+1]}')
print('=-'*50)
print('Os últimos 4 colocados são:')
for u in range(19,15,-1):
    print(f'{u+1}- {classificacao[u]}')
print('=-'*50)
print(f'Os times em ordem alfabética:')
for c in sorted(classificacao):
    print(f'-{c}')
print('=-'*50)
print(f'O chapecoense está em {classificacao.index('Chapecoense') + 1} lugar!')
print('=-'*50)