nome = 'Guanabara'
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretobranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretobranco'], nome, cores['limpa']))

'''
STYLE      TEXT    BACK
0 none      30      40 black
1 bold      31      41 red
4 underline 32      42 green
7 negative  33      43 yellow
            34      44 blue
            35      45 purple
            36      46 cyan
            37      47 white
'''
