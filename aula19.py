# DICIONÁRIO


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos!')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')


#não se dá append em dicionários!
print()
pessoas['peso'] = 95.5 #adicionando nova chave e novo valor
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil) #lista composta por dicionários
print(brasil[0]) #lista composta por dicionários
print(brasil[1]) #lista composta por dicionários
print(brasil[0]['uf'])
print(brasil[0]['sigla'])

estado = dict()
brazilzao = list()

for cont in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brazilzao.append(estado.copy()) #forma de copiar os dados sem usar o fatiamento, que é próprio da lista

print(brazilzao)

for e in brazilzao:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')


