saque = int(input('Qual o valor que deseja sacar? R$ '))
resto = saque
notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0

if saque // 50 != 0:
    notas50 = saque // 50
    resto = saque - notas50 *50
if resto != 0 and resto // 20 != 0:
    notas20 = resto // 20
    resto = resto - notas20 * 20
if resto != 0 and resto // 10 != 0:
    notas10 = resto // 10
    resto = resto - notas10 * 10
if resto != 0 and resto // 1 != 0:
    notas1 = resto // 1
    resto = resto - notas1 * 1

print(f'Ao total, para sacar R${saque:.2f} se usarão:')

if notas50 != 0:
    print(f'- {notas50} nota(s) de 50')
if notas20 != 0:
    print(f'- {notas20} nota(s) de 20')
if notas10 != 0:
    print(f'- {notas10} nota(s) de 10,')
if notas1 != 0:
    print(f'- {notas1} nota(s) de 1')