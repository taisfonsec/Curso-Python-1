n = float(input('Digite um valor em metros: '))
cores = {'numeros':'\033[35m', 'limpa':'\033[m'}
print('Valor em quilômetros: {}{:.2f}km{}\nValor em hectômetros: {}{:.2f}hm{}\nValor em decâmetros: {}{:.2f}dam{}\nValor em decímetros: {}{:.2f}dm{}\nValor em centímetros: {}{:.2f}cm{}\nValor em milímetros: {}{:.2f}mm{}'
      .format(cores['numeros'], n / 1000, cores['limpa'], cores['numeros'], n / 100, cores['limpa'], cores['numeros'], n / 10, cores['limpa'], cores['numeros'], n* 10, cores['limpa'], cores['numeros'], n * 100, cores['limpa'], cores['numeros'], n * 1000, cores['limpa']))