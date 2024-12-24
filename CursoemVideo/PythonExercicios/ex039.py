from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Digite o ano de nascimento: '))
idade = anoAtual - anoNascimento

print('O jovem tem {} anos em {}'.format(idade, anoAtual))

if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    anosFaltando = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(anosFaltando))
    print('Seu alistamento será em {}'.format(anoAtual + anosFaltando))
elif idade > 18:
    anosPassados = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(anosPassados))
    print('Seu alistamento foi em {}'.format(anoAtual - anosPassados))