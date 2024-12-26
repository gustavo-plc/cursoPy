def ficha(nome = 'Desconhecido', gols = 0):

    print(f'O jogador {nome} fez {gols} gol(s)')


#programa principal
nomeJogador = str(input('Digite o nome do jogador: ')).strip()
qtdGols = str(input('Digite quantos gols ele fez: ')).strip()

if qtdGols.isnumeric():
    qtdGols = int(qtdGols)
else:
    qtdGols = 0

if len(nomeJogador) == 0:
    ficha(gols = qtdGols)
else:
    ficha(nomeJogador, qtdGols)

