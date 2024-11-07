from math import sqrt
c1 = int(input('Informe um dos catetos: '))
c2 = int(input('Informe o outro cateto: '))

h = c1**2 + c2**2

print('A hipotenusa é {:.2f}'.format(sqrt(h)))

# ou, de outra forma mais fácil

from math import hypot

c3 = int(input('Informe um dos catetos: '))
c4 = int(input('Informe o outro cateto: '))

print('A hipotenusa é {:.2f}'.format(hypot(c3, c4)))