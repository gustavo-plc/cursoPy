sal = int(input('Escreva seu salário'))

if sal > 1250:
    print('O aumento será de {}'.format(0.1*sal))
    print('O novo salário será de R${}'.format(1.1*sal))
else:
    print('O aumento será de {}'.format(0.15 * sal))
    print('O novo salário será de R$ {}'.format(1.15 * sal))