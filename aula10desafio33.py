n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
n3 = int(input('Escreva mais um número: '))

if n1 > n2:
    if n1 > n3:
        print('O maior número é {}'.format(n1))
    else:
        print('O maior número é {}'.format(n3))
else:
    if n2 > n3:
        print('O maior número é {}'.format(n2))
    else:
        print('O maior número é {}'.format(n3))

