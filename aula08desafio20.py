from random import sample

n1 = input('Escreva o nome do primeiro aluno: ')
n2 = input('Escreva o nome do segundo aluno: ')
n3 = input('Escreva o nome do terceiro aluno: ')
n4 = input('Escreva o nome do quarto aluno: ')

print('A ordem de apresentação será: {}'.format(sample([n1, n2, n3, n4], k=4)))