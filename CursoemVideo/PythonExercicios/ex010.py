#US$1.00 = R$3.27 => Cotação no momento do curso
dinheiro = float(input('Quantos reais você tem na carteira: R$'))
print('Você pode comprar {}US${:.2f}{}'.format('\033[1;32m', dinheiro / 3.27, '\033[m'))