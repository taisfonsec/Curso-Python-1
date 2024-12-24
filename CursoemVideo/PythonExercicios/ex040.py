nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print('A média do aluno é {:.1f}'.format(media))

if media < 5:
    print('Aluno reprovado!')
elif 7 > media >= 5:
    print('Aluno em Recuperação')
else:
    print('Aluno aprovado!')