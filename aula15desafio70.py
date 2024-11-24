import math

soma = 0
mil = 0
barato = math.inf
mais_barato = ' '

while True:
    # primeira leitura de produtos

    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o valor do produto: '))

    # tratamento de exceção do nome sem caracteres

    while nome in {'', ' '}:
        print('Entrada inválida. Digite novamente:  ')
        nome = str(input('Digite o nome do produto: ')).strip()

    # verificação das ĩnformações solicitadas:

    if preco > 1000:
        mil += 1
    soma += preco
    if preco <= barato:
        barato = preco
        mais_barato = nome

    # laço externo para saber se o usuário quer continuar

    mais = str(input('Deseja entrar com mais dados?  (S/N)')).lower().strip()
    while mais not in {'s', 'n'}:
        print('Entrada inválida. Digite novamente no formato (S)im ou (N)ão:  ')
        mais = str(input('Deseja entrar com mais dados?  (S/N)')).lower().strip()

    if mais == 'n':
        print('Obrigado por utilizar nosso programa!\n')
        break

print(f'O total gasto na compra foi de R$ {soma}')
print(f'{mil} produtos custam mais de mil reais!')
print(f'{mais_barato} é o produto mais barato!')
