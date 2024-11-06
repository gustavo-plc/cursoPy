from math import sqrt
c1 = int(input('Informe um dos catetos: '))
c2 = int(input('Informe o outro cateto: '))

h = c1**2 + c2**2

print('A hipotenusa é {}'.format(sqrt(h)))