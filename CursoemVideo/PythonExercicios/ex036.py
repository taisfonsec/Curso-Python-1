valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?: '))

mensalidade = valorCasa/(anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos,'.format(valorCasa, anos), end='')
print(' o valor da prestação mensal será de R${:.2f}'.format(mensalidade))

if mensalidade <= (salario * 0.3):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')