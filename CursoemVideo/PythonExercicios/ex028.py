from random import randint
from time import sleep

print('Pensando...')
escolhido = randint(0, 5)
sleep(3)

tentativa = int(input('Pensei em um numero entre 0 e 5. Advinhe qual foi: '))
print('Processando...')
sleep(3)

print('O número pensado foi {}'.format(escolhido))
if tentativa == escolhido:
    print('Parabéns! Você venceu!')
else:
    print('Que pena! Você perdeu!')