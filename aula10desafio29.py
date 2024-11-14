vel = int(input('Escreva a velocidade do carro: '))

if vel > 80:
    print('Você foi multado!')
    print('Sua multa é {} reais!'.format((vel-80)*7))
