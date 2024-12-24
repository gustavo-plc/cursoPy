from time import sleep

def maior(*a):
    print('-=' *30)
    print('Analisando os valores passados...')
    for i in range (0, len(a)):
        print(f'{a[i]}', end = ' ')
        sleep(0.5)
    print()
    print(f'{f'Foram informados {len(a)} valores ao todo'}')
    print(f'{f'O maior valor informado foi {max(a)}'}')

maior(4, 6, 2, 3, 0, 8, 9)
maior(4, 6, 2, 7)
maior(2, 4)
maior(1)