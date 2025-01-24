num = int(input('Digite um número: '))
c = num
fatorial = 1

print('{}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print('{}'. format(fatorial))


from math import factorial
num = int(input('Digite um número: '))
fatorial = factorial(num)

print('O fatorial de {} é {}'.format(num, fatorial))

'''
num = int(input('Digite um número: '))
fatorial = 1

print('{}! = '.format(num), end='')
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
print('{}'. format(fatorial))
'''