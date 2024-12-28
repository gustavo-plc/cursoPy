import moeda

valor = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor)}')
print(f'Aumentando {moeda.moeda(valor)} de {'20'}% temos {moeda.aumentar(valor, 20, True)}')
print(f'Diminuindo {moeda.moeda(valor)} de {'15'}% temos {moeda.diminuir(valor, 15)}')