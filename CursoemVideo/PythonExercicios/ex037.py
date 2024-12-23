numero = int(input('Digite um número inteiro: '))
print('''Bases de conversão:
[1] Binário
[2] Octal
[3 Hexadecimal''')
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertendo para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertendo para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opçãp inválida! Tente Novamente.')