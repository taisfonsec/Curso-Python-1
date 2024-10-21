velocidade = float(input('Digite a velocidade do carro (Km/h): '))

if velocidade > 80:
    print('Você foi multado! Ultrapassou o limite de velocidade de 80Km/h.')
    multa = (velocidade - 80) * 7.0
    print('Valor da multa: R${:.2f}'.format(multa))
print('Dirija sempre com segurança!')