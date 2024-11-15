l1 = int(input('Digite o comprimento de um lado: '))
l2 = int(input('Digite o comprimento de outro lado: '))
l3 = int(input('Digite o comprimento de mais um lado: '))

#condição de existência: a soma de quaisquer dois lados deve ser maior que o terceiro lado

if l1 + l2 > l3:
    if l2 + l3 > l1:
        if l3 + l1 > l2:
            print('esse triângulo existe!')
            if l1 == l2 == l3:
                print('Triângulo equilátero')
            elif l1 == l2 or l2 == l3 or l3 == l1:
                print('Triângulo isóceles')
            else:
                print('Triângulo escaleno')
        else:
            print('Não existe triângulo com esses lados')
    else:
        print('Não existe triângulo com esses lados')
else:
    print('Não existe triângulo com esses lados')