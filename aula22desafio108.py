import moeda

valor = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando {moeda.moeda(valor)} de {'20'}% temos {moeda.moeda(moeda.aumentar(valor, 20))}')
print(f'Diminuindo {moeda.moeda(valor)} de {'15'}% temos {moeda.moeda(moeda.diminuir(valor, 15))}')