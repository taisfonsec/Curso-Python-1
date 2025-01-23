from random import randint
from time import sleep

print('Pensando...')
escolhido = randint(0, 10)
sleep(3)
print('Pensei em um numero entre 0 e 10.')

acertou = False
palpites = 0

while not acertou:
    tentativa = int(input('Advinhe qual foi: '))
    palpites += 1
    if tentativa == escolhido:
        acertou = True
    else:
        if tentativa < escolhido:
            print('Mais... Tente novamente.')
        elif tentativa > escolhido:
            print('Menos... Tente Novamente.')
print('Parabéns! Você venceu com {} palpites!'.format(palpites))