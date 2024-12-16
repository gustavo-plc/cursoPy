mtl = list()

for i in range(0, 3):
    for j in range (0, 3):
        mtl.append(int(input(f'Digite um valor para [{i},{j}]: ')))

for c in range (0, 3):
    print(f'[{mtl[c]}] ', end = '')
print(' ')

for c in range (3, 6):
    print(f'[{mtl[c]}] ', end = '')

print(' ')
for c in range(6, 9):
    print(f'[{mtl[c]}] ', end = '')

print(' ')