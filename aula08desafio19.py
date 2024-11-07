import random

n1 = input('Escreva o nome do primeiro aluno: ')
n2 = input('Escreva o nome do segundo aluno: ')
n3 = input('Escreva o nome do terceiro aluno: ')
n4 = input('Escreva o nome do quarto aluno: ')

print('O aluno escolhido foi {}'.format(random.choice([n1, n2, n3, n4])))