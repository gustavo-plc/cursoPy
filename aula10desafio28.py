import random

a = random.randint(0,5)

b = int(input('acerte o número que o computador pensou! Qual foi?  '))

if a == b:
    print('Acertô, miserávi')
else:
    print('Errou!')
