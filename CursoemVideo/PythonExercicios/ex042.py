segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

if segmento1 < (segmento2 + segmento3) and segmento2 < (segmento1 + segmento3) and segmento3 < (segmento1 + segmento2):
    print('Os segmentos podem formar um triângulo ', end='')

    if segmento1 == segmento2 == segmento3:
        print('EQUILÁTERO!')
    elif segmento1 != segmento2 !=segmento3 !=segmento1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos não podem formar um triângulo!')