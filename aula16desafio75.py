tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
print(f'O número 3 apareceu primeiramente na posição {tupla.index(3)}.' if tupla.count(3) == True else 'O número 3 não apareceu!')

print('Os números pares foram: ', end='')
for i in range(0,4):
    print(f' {tupla[i]} ' if tupla[i] % 2 == 0 else '', end = '')
