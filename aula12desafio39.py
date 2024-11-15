import datetime
ano = int(input('Digite o ano do seu nascimento!: \n'))
ano_atual = datetime.datetime.now().year

idade = ano_atual - ano

if idade < 18:
    print('Você ainda vai se alistar ao serviço militar, e falta(m) {} ano(s)'.format(18-idade))
elif idade == 18:
    print('Você precisa se alistar neste ano!')
else:
    print('Já passou {} ano(s) para você se alistar'.format(idade-18))
