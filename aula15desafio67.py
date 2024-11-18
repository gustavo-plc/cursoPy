n = int(input('Digite um número para ver sua tabuada ou um número negativo para sair: '))

while n > 0:
    for i in range (1,11):
        print(f'{n} X {i} = {n*i}')
    n = int(input('Digite um número para ver sua tabuada ou um número negativo para sair: '))
print('Fim')