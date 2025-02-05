from random import randint
from time import sleep

lista = list()
resultados = {'Nome': '', 'Valor': 0}

print('Valores Sorteados: ')
for i in range (0,4):
    resultados['Nome'] = f'Jogador {i+1}'
    resultados['Valor'] = randint(1, 6)
    lista.append(resultados.copy())
    print(f'O jogador {lista[i]['Nome']} tirou {lista[i]['Valor']}')
    sleep(1)

print('Ranking: ')

ordenada = sorted(lista, key=lambda x: x['Valor'], reverse = True)

#também é possível ordenar dicionários:
#se eu não tivesse criado uma lista auxiliar, mas sim um
#dicionário auxiliar, para ordená-lo
#seria dessa forma:

# ordenada = sorted(resultados.items(), key = itemgetter(1), reverse = True)

for i in range(0,4):
    print(f'O jogador {ordenada[i]['Nome']} tirou {ordenada[i]['Valor']}')
    sleep(1)