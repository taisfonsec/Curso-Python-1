n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
termo = n1
total = 0
maisTermos = 10

while maisTermos != 0:
    total = total + maisTermos
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        c += 1
    print('Pausa')
    maisTermos = int(input('Quantos termos você quer mostrar a mais?: '))
print('Progressão aritmética finalizada com {} termos'.format(total))