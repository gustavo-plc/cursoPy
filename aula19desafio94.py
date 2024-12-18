pessoas = dict()
lista = list()

while True:
    pessoas['nome'] = str(input('Nome: ')).strip()
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().lower()
    while pessoas['sexo'] not in {'m', 'f'}:
        print('Formato inválido!')
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().lower()
    pessoas['idade'] = int(input('Idade: '))
    cont = str(input('Quer continuar? [S/N] ')).lower().strip()
    while cont not in {'s', 'n'}:
        print('Formato inválido!')
        cont = str(input('Quer continuar? [S/N] ')).lower().strip()
    lista.append(pessoas.copy())
    if cont == 'n':
        print(f'O grupo tem {len(lista)} pessoas')
        tot = 0
        for i in range(0, len(lista)):
            tot += lista[i]['idade']
        avg = tot/len(lista)
        print(f'A média de idade é de {avg} anos')
        print('As mulheres cadastradas foram: ', end = ' ')

        for i in range(0, len(lista)):
            if lista[i]['sexo'] == 'f':
                print(f'{lista[i]['nome']}', end = ' ')
        print()
        print('Lista das pessoas que estão acima da média de idade: ')
        for i in range(0, len(lista)):
            if lista[i]['idade'] > avg:
                print(f'{lista[i]['nome']} tem {lista[i]['idade']} anos! ')
        break