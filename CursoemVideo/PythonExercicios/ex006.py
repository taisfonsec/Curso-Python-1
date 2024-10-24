n = int(input('Digite um número: '))
cores = {'numeros':'\033[1;33m', 'limpa':'\033[m'}
print('O seu dobro é {}{}{}, o seu triplo é {}{}{} e sua raiz quadrada é {}{:.2f}{}'. format(cores['numeros'], n * 2, cores['limpa'], cores['numeros'], n * 3, cores['limpa'], cores['numeros'], pow(n, (1/2)), cores['limpa']))