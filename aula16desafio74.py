from random import randint
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(tupla)
maiormenor = sorted(tupla)
maior = maiormenor[4]
menor = maiormenor[0]
print(f'O menor valor da tupla é {menor} e o maior valor é {maior}.')
