def contador():
    for i in range (0, 10):
        print(f'{i+1}', end = ' ')
    print()
    for t in range (11, 0, -2):
        print(f'{t-1}', end = ' ')
    print()
    inicio = int(input('Informe o início: '))
    fim = int(input('Informe o fim: '))
    passo = int(input('Informe o passo: '))
    for u in range (inicio, fim, passo):
        print(f'{u}', end = ' ')
    print()

#programa principal


contador()