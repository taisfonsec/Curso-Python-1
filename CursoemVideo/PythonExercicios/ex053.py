frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juncao = ''.join(palavras)
inverso = ''
inverso = juncao[::-1]

'''
for letra in range(len(juncao) - 1, -1, -1):
    inverso += juncao[letra]
'''
print('O inverso de {} é {}'.format(juncao, inverso))
if inverso == juncao:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')