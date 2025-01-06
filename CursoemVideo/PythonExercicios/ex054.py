from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pesssoa nasceu?: '.format(i)))
    idade = anoAtual - nascimento

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('{} são pessoas maiores de idade'.format(maior))
print('{} são pessoas menores de idade'. format(menor))