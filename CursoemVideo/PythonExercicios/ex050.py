soma = 0
cont = 0

for c in range(1, 7):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você digitou {} números pares e a soma foi {}'.format(cont, soma))