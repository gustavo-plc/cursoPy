lista = list()

for i in range (0, 5):
    lista.append(int(input('Digite um valor para a lista: ')))

print(f'O maior valor da lista é {max(lista)} e ocupa as posições: ', end = '')
for i, v in enumerate(lista):
    print(f'{i}...' if v == max(lista) else '', end = '')

print(' ')

print(f'O menor valor da lista é {min(lista)} e ocupa as posições: ', end = '')
for i, v in enumerate(lista):
    print(f'{i}...' if v == min(lista) else '', end = '')
