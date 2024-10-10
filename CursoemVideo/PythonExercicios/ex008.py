n = float(input('Digite um valor em metros: '))
print('Valor em quilômetros: {:.2f}km\nValor em hectômetros: {:.2f}hm\nValor em decâmetros: {:.2f}dam\nValor em decímetros: {:.2f}dm\nValor em centímetros: {:.2f}cm\nValor em milímetros: {:.2f}mm'
      .format(n / 1000, n / 100, n / 10, n* 10, n * 100, n * 1000))