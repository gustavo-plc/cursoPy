n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: (999 para parar)\n'))
    if n == 999:
        break
    soma += n
    c += 1
print(f'Foram digitados {c} números ea a soma entre eles é {soma}')