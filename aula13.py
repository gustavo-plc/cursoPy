#laços de repetição: for


for i in range (1,6): #pára antes do 6, não considera o último número
    print('Oi')
    print(i)
print('Fim!')

for c in range (6, 0, -1): # (início, fim, passo)
    print(c)

for c in range (6, 0, -2): # (início, fim, passo)
    print(c)

for c in range (0, 50, 4): # (início, fim, passo)
    print(c)

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for i in range (i, f+1, p):
    print(i)

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('O somatório dos números inseridos é {}'.format(s))