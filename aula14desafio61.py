a1 = int(input('Informe o primeiro termo da PA: \n'))
r = int(input('Informe a razão da PA: \n'))
c = 0

while c < 9:
    an = a1 + c*r
    print('a{}'.format(c+1) + ' = ' + '{}'.format(an))
    c += 1

mais = 1

while mais > 0:
    while c < c + mais:
        an = a1 + c*r
        print('a{}'.format(c+1) + ' = ' + '{}'.format(an))
        c += 1
        mais -= 1
    mais = int(input('Digite quantos termos deseja ver a mais: \n'))

