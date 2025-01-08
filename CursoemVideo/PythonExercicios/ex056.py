somaIdade = 0
mediaIdade = 0
nomeHomemVelho = ''
maiorIdadeHomem = 0
totalMulher = 0


for p in range(1, 5):
    print('--- {}ª Pessoa ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()

    somaIdade += idade
    if p == 1 and sexo == 'M':
        nomeHomemVelho = nome
        maiorIdadeHomem = idade
    if sexo == 'M' and idade > maiorIdadeHomem:
        nomeHomemVelho = nome
        maiorIdadeHomem = idade
    if sexo == 'F' and idade < 20:
        totalMulher += 1

mediaIdade = somaIdade / 4
print('A média de idade do grupo é {} anos'.format(mediaIdade))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeHomemVelho))
print('O total de mulheres com menos de 20 anos é {}'.format(totalMulher))