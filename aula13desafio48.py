c = 0
for i in range (1,501):
    if i % 3 == 0 and i % 2 != 0:
        c = c + i
print('A soma dos valores é {}'.format(c))