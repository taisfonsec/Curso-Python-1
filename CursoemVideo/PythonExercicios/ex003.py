n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número:' ))
s = n1 + n2
cores = {'numeros':'\033[1;32m', 'limpa':'\033[m'}
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}'.format(cores['numeros'],n1, cores['limpa'], cores['numeros'], n2, cores['limpa'], cores['numeros'], s, cores['limpa']))