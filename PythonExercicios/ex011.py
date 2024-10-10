largura = float(input('Largura da parede(m): '))
altura = float(input('Altura da parede(m): '))
area = largura * altura
tinta = area / 2

print('Área total: {:.2f}m²\nA quantidade de tinta necessária é de {:.1f}L'.format(area, tinta))