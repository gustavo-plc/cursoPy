km = int(input('Digite a distância da viagem em km: '))
if km<=200:
    print('O preço da passagem é R${:.2f}'.format(0.5*km))
else:
    print('O preço da passagem é R${:.2f}'.format(0.45*km))