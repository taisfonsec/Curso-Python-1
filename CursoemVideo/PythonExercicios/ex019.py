from random import choice
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
listaNomes = [n1, n2, n3, n4]
escolhido = choice(listaNomes)
print('O aluno escolhido para apagar o quadro foi o(a) {}'.format(escolhido))