print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('Preço total das compras: R$'))
print('''Formas de Pagamento:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    total = preco - (preco * 0.1)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.2)
    totalParcela = int(input('Em quantas parcelas?: '))
    parcela = total / totalParcela
    print('Sua compra foi parcelada em {}x de R${:.2f} com juros'.format(totalParcela, parcela))
else:
    total = 0
    print('Opção inválida! Tente novamente.')
print('O total de sua compra será de R${:.2f} com os descontos'.format(total))