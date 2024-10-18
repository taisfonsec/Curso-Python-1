nome = str(input('Digite seu nome completo: '))
print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))

dividido = nome.split()
juntado = ''.join(dividido)

print('Total de letras: {}'.format(len(juntado)))
print('Total de letras do primeiro nome: {}'.format(len(dividido[0])))