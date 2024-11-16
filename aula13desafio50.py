vet = [1, 2, 3, 4, 5, 6]
s = 0
for i in range (0,6): #preenchimento da lista
    vet[i] = int(input('Digite um número: '))
    if vet[i] % 2 == 0:
        s = s + vet[i]
print('A soma dos números pares digitados é {}'.format(s))
