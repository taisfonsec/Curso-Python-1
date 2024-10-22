salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250:
    salarioNovo = salario + (salario * 0.10)
else:
    salarioNovo = salario + (salario * 0.15)

print('O novo salário do funcionário será R${:.2f}'.format(salarioNovo))