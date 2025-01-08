maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Pedo da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso informado foi {}Kg'.format(maior))
print('O menor peso informado foi {}Kg'.format(menor))