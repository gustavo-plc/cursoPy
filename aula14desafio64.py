c = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    c += 1
    soma += n
print('Foram digitados {} números e a soma entre eles é {}'.format(c-1, soma-999))