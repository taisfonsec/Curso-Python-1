n = int(input('Digite um número: '))
cores = {'numeros':'\033[30;47m', 'limpa':'\033[m'}
print('{}1 X {} = {}{}\n{}2 X {} = {}{}\n{}3 X {} = {}{}\n{}4 X {} = {}{}\n{}5 X {} = {}{}\n{}6 X {} = {}{}\n{}7 X {} = {}{}\n{}8 X {} = {}{}\n{}9 X {} = {}{}\n{}10 X {} = {}{}'
      .format(cores['numeros'],n, n * 1,cores['limpa'],
               cores['numeros'], n, n * 2, cores['limpa'],
                cores['numeros'], n, n * 3, cores['limpa'],
                 cores['numeros'], n, n * 4, cores['limpa'],
                  cores['numeros'], n, n * 5, cores['limpa'],
                   cores['numeros'], n, n * 6, cores['limpa'],
                    cores['numeros'], n, n * 7, cores['limpa'],
                     cores['numeros'], n, n * 8, cores['limpa'],
                      cores['numeros'], n, n * 9, cores['limpa'],
                      cores['numeros'], n, n * 10, cores['limpa']))