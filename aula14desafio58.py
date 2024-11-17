import random

a = random.randint(0,10)
b = int(input('acerte o número que o computador pensou! Qual foi?  '))
c = 1
while b != a:
    b = int(input('Tente outro palpite! '))
    c += 1

print('Acertô, miserávi! E foram necessárias {} tentativas!'.format(c))

