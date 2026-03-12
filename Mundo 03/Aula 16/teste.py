lanches = ('batata frita', 'hamburguer', 'coca', 'sorvete')
print(lanches)

print(sorted(lanches)) #organiza em ordem de tamanho
for c in (lanches):
    print(c)
# for c in range (0, len(lanche)):
#   print(lanche[cont])
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')
lanches[1] = 'onion rings'
