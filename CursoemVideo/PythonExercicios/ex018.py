from math import radians, sin, cos, tan
angulo = int(input('Digite um ângulo: '))
rad = radians(angulo)
sen = sin(rad)
cos = cos(rad)
tang = tan(rad)
print('O seno, cosseno e tangente do ângulo {} são, respectivamente:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(angulo, sen, cos, tang))