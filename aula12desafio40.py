
n1 = int(input('escreva a primeira nota\n'))
n2 = int(input('escreva a segunda nota\n'))

media = (n1 + n2)/2

if media < 5:
    print('REPROVADO!')
elif media >= 5 and media < 7:
    print('RECUPRAÇÃO!')
else:
    print('APROVADO!!')
