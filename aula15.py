n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
#ou, com f strings

print(f'a soma vale {s}') #com variável dentro das chaves
