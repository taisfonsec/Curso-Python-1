n = int(input('Digite um número: '))
cores = {'sucessor':'\033[0;32m', 'antecessor':'\033[0;31m', 'limpa':'\033[m'}
print('O seu sucessor é {}{}{} e seu antecessor é {}{}{}'.format(cores['sucessor'], n + 1, cores['limpa'], cores['antecessor'], n - 1, cores['limpa']))