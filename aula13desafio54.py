from datetime import date

ano = date.today().year
maiores = 0
menores = 0

for i in range(0, 6):
    p = int(input('Digite o ano de seu nascimento: \n'))
    if ano - p >= 21:
        maiores += 1
    else:
        menores += 1
print('O total de maiores de idade é de {}'.format(maiores))
print('O total de menores de idade é de {}'.format(menores))