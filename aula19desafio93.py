jogador = dict()

jogador['nome'] = str(input('Digite o nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

gols = list()
jogador['total'] = 0

for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols ele fez na partida {i+1}? ')))
    jogador['total'] += gols[i]

#ou jogador['total'] = sum(gols)

jogador['gols'] = gols[:]

print('-#-' *20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-#-' *20)

print(f'O jogador {jogador['nome']} jogou {partidas} partidas!')

for i in range(0, partidas):
    print(f'Na partida {i+1}, fez {gols[i]} gols. ')

print(f'Foi um total de {jogador['total']} gols! ')