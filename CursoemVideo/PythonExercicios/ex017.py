from math import hypot
catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa vale {:.2f}'.format(hipotenusa))