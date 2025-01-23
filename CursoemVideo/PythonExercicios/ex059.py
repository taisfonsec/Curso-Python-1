from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        soma = num1 + num2
        print('{} + {} = {}'.format(num1, num2, soma))
    elif opcao == 2:
        produto = num1 * num2
        print('{} x {} = {}'.format(num1, num2, produto))
    elif opcao == 3:
        maior = 0
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior número é {}'.format(maior))
    elif opcao == 4:
        print('Informe os novos números:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa!')
