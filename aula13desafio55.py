mor = -float('inf')  # Inicializa com o valor mais baixo possível
mnr = float('inf')   # Inicializa com o valor mais alto possível

for i in range (0, 5):
    peso = float(input('Escreva seu peso: \n'))
    if peso > mor:
        mor = peso
    if peso < mnr:
        mnr = peso
print('O maior peso é {}'.format(mor))
print('O menor peso é {}'.format(mnr))
