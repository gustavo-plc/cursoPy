n = int(input('Quantos elementos da sequência de Fibonacci você quer ver? '))

a1 = 0
a2 = 1
c = 3

# 0->1->1->2->3->5->8

if n == 1:
    print('{}->'.format(a1), end = '')
elif n == 2:
    print('{}->{}'.format(a1, a2), end = '')
else:
    print('{}->{}->'.format(a1, a2), end = '')
    while c <= n:
        a3 = a1 + a2
        print('{}->'.format(a3), end='')
        a1 = a2
        a2 = a3
        c += 1
print('FIM!')
