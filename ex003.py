n1 = input('Escreva um número: ') #o retorno da função input é sempre uma string
n2 = input('Escreva outro número: ')
s = n1 + n2

print('O resultado da soma é: ',s)

# corrigindo:

n3 = int(input('Escreva um número: ')) #casting, para ler como inteiro)
n4 = int(input('Escreva outro número: '))
s2 = n3 + n4

print('O resultado da soma é: ',s2)

print('O resultado da soma é :{}' .format(s2))