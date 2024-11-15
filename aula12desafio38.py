n1 = int(input('escreva um numero inteiro\n'))
n2 = int(input('escreva outro numero inteiro\n'))

if n1 > n2:
    print('O primeiro valor, {}, é maior'.format(n1))
elif n2 > n1:
    print('O segundo valor, {}, é maior'.format(n2))
else:
    print('Os valores são iguais!')