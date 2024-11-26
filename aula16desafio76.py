listagem = ('Lápis', 1.80, 'Borracha', 0.60, 'Apontador', 3.20, 'Caneta', 1.50, 'Lapiseira', 10.50, 'Caderno', 14, 'Estojo', 25, 'Mochila', 300)

print('TABELA DE PRODUTOS'.center(58, '*'))
for i in range (0, 16, 2):
    print('{:.<50}'.format(listagem[i]), end = '')
    print('R$ ' + '{:9>.2f}'.format(listagem[i+1]))



