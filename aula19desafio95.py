jogador = dict() #dados individuais
jogadores = list() #dados gerais
#ideia: haverá uma lista externa, composta por dicionários
#cada dicionário será de um jogador, contendo nome, partidas, [gols em cada partida]
#gols em cada partida será uma lista

while True:
    jogador['nome'] = str(input('Digite o nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

    gols = list()
    jogador['total'] = 0

    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols ele fez na partida {i+1}? ')))
        jogador['total'] += gols[i]

    #ou jogador['total'] = sum(gols)

    jogador['gols'] = gols[:]
    jogadores.append(jogador.copy())
    print(jogadores)
    print(jogador)
    cont = str(input('Deseja continuar? [S/N] ')).lower().strip()
    while cont not in {'s', 'n'}:
        print('Formato inválido!')
        cont = str(input('Deseja continuar? [S/N] ')).lower().strip()
    if cont == 'n':
        print('--' *30)
        print(f'{'COD.':<5}', end = '')
        print(f'{'NOME':<20}', end = '')
        print(f'{'GOLS':<20}', end = '')
        print(f'{'TOTAL':<3}')
        print('--' *30)
        for c in range(0, len(jogadores)): #laço que vai percorrer a lista externa, dos jogadores em geral
            print(f'{c:<5}', end='')
            print(f'{jogadores[c]['nome']:<20}', end='')
            print(f'{str(jogadores[c]['gols']):<20}', end='') #para formatar na quantidade de caracteres, foi preciso transformar em string
            print(f'{jogadores[c]['total']:<3}')

        while True:
            det = int(input('Mostrar dados de qual jogador? Digite 999 para sair '))
            if det == 999:
                print('FIM')
                break
            if det not in range(0, len(jogadores)):
                print(f'ERRO! O jogador {det} não foi encontrado! Tente novamente! ')
            else:
                print(f'LEVANTAMENTO DO JOGADOR: {jogadores[det]['nome']} ')
                for i in range(0, len(jogadores[det]['gols'])):
                    print(f'Na partida {i + 1}, fez {jogadores[det]['gols'][i]} gols. ')
        break