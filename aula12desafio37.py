num = int(input('escreva um número inteiro: '))
base = int(input('Escolha a base numérica para conversão: \n1- Binário\n2- Octal\n3- Hexadecimal\n'))

if base == 1:
    if num == 0:
        print('O número em binário é 0')  # Caso especial para 0
    else:
        st = ''
        while num > 0:
            st = str(num % 2) + st  # Acumula os restos das divisões
            num = num // 2  # Divide o número por 2, sem o resto
    print('O número em binário é {}'.format(st))

if base == 2:
    if num == 0:
        print('O número em octal é 0')  # Caso especial para 0
    else:
        st = ''
        while num > 0:
            st = str(num % 8) + st  # Acumula os restos das divisões
            num = num // 8
    print('O número em octal é {}'.format(st))

if base == 3:
    if num == 0:
        print('O número em hexadecimal é 0')  # Caso especial para 0
    else:
        st = ''
        while num > 0:
            if num % 16 > 9:
                dic = {
                    10: 'A',
                    11: 'B',
                    12: 'C',
                    13: 'D',
                    14: 'E',
                    15: 'F'
                }
                st = str(dic[num % 16]) + st  # Acumula os restos das divisões
                num = num // 16
            else:
                st = str(num % 16) + st  # Acumula os restos das divisões
                num = num // 16
    print('O número em hexadecimal é {}'.format(st))