distancia = float(input('Qual a distância da viagem em Km?: '))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
'''
if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia
'''
print('Preço da passagem: R${:.2f}'.format(preco))