valor = int(input('Qual será o valor a ser sacado?\n'))

#temos cédulas de 50, 20, 10 e 1

n50 = valor // 50
valor %= 50
n20 = valor // 20
valor %= 20
n10 = valor // 10
valor %= 10
n1 = valor

if n50 != 0:
    print(f'Serão entregues {n50} notas de R$ 50')
if n20 != 0:
    print(f'Serão entregues {n20} notas de R$ 20')
if n10 != 0:
    print(f'Serão entregues {n10} notas de R$ 10')
if n1 != 0:
    print(f'Serão entregues {n1} notas de R$ 1')
