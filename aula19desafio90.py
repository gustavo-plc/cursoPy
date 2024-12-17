#aluno = {'Nome': '', 'Média': 0, 'Situação': ''}
#não precisa inicializar, pois na atribuição dos valores
#o dicionário já cria as chaves
aluno= dict()

aluno['Nome'] = str(input('Informe o nome do aluno: ')).strip()
aluno['Média'] = float(input(f'Qual a média de {aluno['Nome']}? '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print()
for k, v in aluno.items():
    print(f'{k} é {v}')
