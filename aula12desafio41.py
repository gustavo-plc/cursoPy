import datetime
ano = int(input('Digite o ano do seu nascimento!: \n'))
ano_atual = datetime.datetime.now().year

idade = ano_atual - ano

if idade <= 9:
    print('A categoria do atleta é Mirim')
elif idade > 9 and idade <= 14:
    print('A categoria do atleta é Infantil')
elif idade > 14 and idade <= 19:
    print('A categoria do atleta é Junior')
elif idade > 19 and idade <= 20:
    print('A categoria do atleta é Sênior')
else:
    print('A categoria é master')