from random import randint
from time import sleep

numeros = list()

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        numeros.append(randint(1,10))
        print(f'{numeros[i]}', end = ' ')
        sleep(0.3)
    print('PRONTO !')

def somaPar():
    soma = 0
    for i in range(0, len(numeros)):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
    print(f'A soma de todos os valores pares de {numeros} é: {soma}')


sorteia()

somaPar()