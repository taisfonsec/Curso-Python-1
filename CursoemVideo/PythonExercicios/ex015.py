quilometros = float(input('Quantos quilômetros(Km) o carro percorreu?: '))
dias = int(input('Por quantos dias o carro foi alugado?: '))
preco = (60 * dias) + (quilometros * 0.15)
print('O total a pagar é de R${:.2f}'.format(preco))