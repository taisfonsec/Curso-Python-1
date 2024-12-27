from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Jogadas:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha uma jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: #PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Vitória do Jogador!')
    elif jogador == 2:
        print('Vitória do Computador!')
    else:
        print('Jogada inválida!')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('Vitória do Computador!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Vitória do Jogador!')
    else:
        print('Jogada inválida!')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('Vitória do Jogador!')
    elif jogador == 1:
        print('Vitória do Computador!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida!')