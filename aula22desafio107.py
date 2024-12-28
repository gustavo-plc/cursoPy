import moeda

valor = float(input('Digite um preço: '))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando {valor} de {'20'}% temos {moeda.aumentar(valor, 20)}')
print(f'Diminuindo {valor} de {'15'}% temos {moeda.diminuir(valor, 15)}')
