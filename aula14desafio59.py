m = 0

n1 = int(input('Digite um valor: \n'))
n2 = int(input('Digite outro valor: \n'))

while m != 5:
    print('1- Somá-los')
    print('2- Multiplicá-los')
    print('3- Qual o maior?')
    print('4- Escrever novos números')
    print('5- Sair do jogo\n')
    m = int(input('Escolha uma opção: \n'))
    if m == 1:
        print('A soma é {}\n'.format(n1+n2))
    if m == 2:
        print('A multiplicação é {}\n'.format(n1*n2))
    if m == 3:
        if n1 > n2:
            print('O maior é {}\n'.format(n1))
        elif n2 > n1:
            print('O maior é {}\n'.format(n2))
        else:
            print('São iguais!\n')
    if m == 4:
        n1 = int(input('Digite um valor: \n'))
        n2 = int(input('Digite outro valor: \n'))
print('\nFoi bom ter você aqui conosco!')
