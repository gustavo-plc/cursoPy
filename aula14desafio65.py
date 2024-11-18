
n = int(input('Digite um número: '))
resp = input('Quer continuar? (S/N)').strip().lower()
soma = n
c = 1
maior = n
menor = n

while resp == 's':
    p = int(input('Digite um número: '))
    soma += p
    c += 1
    if p > n:
        maior = p
    else:
        menor = p
    resp = input('Quer continuar? (S/N)').strip().lower()
print('A média é {}, o maior é {} e o menor é {}'.format(soma/c, maior, menor))