from datetime import datetime
pessoa = dict()
ano = datetime.now().year

pessoa['Nome'] = str(input('Digite seu nome: ').strip())
dn = int(input('Data de nascimento: '))
pessoa['Idade'] = ano - dn
pessoa['Nº da CTPS'] = int(input('Nº CTPS: (0 caso não tenha) '))

if pessoa['Nº da CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['Salário'] = float(input('Digite o salário: '))
    pessoa['Ano que aposenta'] = pessoa['Ano de contratação'] - dn + 35

for k, v in pessoa.items():
    print(f'{k} é {v}')
