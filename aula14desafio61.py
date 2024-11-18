a1 = int(input('Informe o primeiro termo da PA: \n'))
r = int(input('Informe a razão da PA: \n'))
c = 0

while c <= 10:
    an = a1 + c*r
    print('a{}'.format(c) + ' = ' + '{}'.format(an))
    c += 1
