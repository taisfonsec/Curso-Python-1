sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dado inválido! Por favor, digite seu sexo novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))