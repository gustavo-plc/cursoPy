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