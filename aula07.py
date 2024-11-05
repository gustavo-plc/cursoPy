#ordem de precedência de operadores
# ()
# **
# *, /, //, %
# +, -

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:20}!'.format(nome)) #em 20 espaços
print('Prazer em te conhecer, {:>20}!'.format(nome)) #alinhado à direita
print('Prazer em te conhecer, {:<20}!'.format(nome)) #alinhado à esquerda
print('Prazer em te conhecer, {:^20}!'.format(nome)) #Centralizado
print('Prazer em te conhecer, {:-^20}!'.format(nome)) #Centralizado e preenchendo espaços com caractere

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

print('A soma vale {}'.format(n1+n2)) #sem utilização de uma terceira variável

n3 = int(input('Um valor: '))
n4 = int(input('Outro valor: '))

s = n3+n4
m = n3*n4
d = n3/n4
di = n3//n4
e = n1**n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d),end=' ') #impedindo quebra de linha
print('Divisão inteira {} e potência {}'.format(di, e))