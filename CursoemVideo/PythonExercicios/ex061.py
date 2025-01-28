n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
termo = n1

while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    c += 1
print('Fim')