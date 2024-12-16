matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for i in range(0, 3):
    for j in range (0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i},{j}]: '))


for i in range(0, 3):
    for j in range (0, 3):
        print(f'[{matriz[i][j]:^5}]', end = '')
    print()

soma = 0
for i in range(0, 3):
    for j in range (0, 3):
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]

soma3ac = 0

for i in range(0, 3):
    for j in range (2, 3):
        soma3ac += matriz[i][j]

maior = matriz[1][0]
for i in range(1, 2):
    for j in range(0, 3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]


print(f'A soma de todos os valores pares digitados é: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma3ac}')
print(f'O maior valor da segunda linha é: {maior}')
