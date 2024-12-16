from random import sample
from time import sleep

print('-' *30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' *30)

qtd = int(input('Para quantos jogos deseja sugestão? '))

for cont in range(0, qtd):
    jogo = sample(range(1,61), 6) #já gera os números em uma lista
    jogo.sort()
    print(f'Jogo {cont + 1}: {jogo} ')
    sleep(1)

print(f'{'BOA SORTE!':^30}')