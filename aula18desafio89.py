# lista geral = [[nome, [n1, n2], média], [nome, [n1, n2], média]]

lista = list()
alunos = ['', [], 0]
notas = [0, 0]

while True:
    alunos[0] = (str(input('Digite o nome do aluno: ')).strip())
    notas[0] = (float(input('Nota 1: ')))
    notas[1] = (float(input('Nota 2: ')))
    alunos[1] = notas[:]
    alunos[2] = (notas[0]+notas[1])/2
    lista.append(alunos[:])
    cont = str(input('Deseja continuar? (S/N) ')).lower().strip()
    while cont not in {'s', 'n'}:
        print('Formato inválido!')
        cont = str(input('Deseja continuar? (S/N) ')).lower().strip()
    if cont == 'n':
        print('-=' *30)
        print(f'{'Nº':^5}{'Nome':^20}{'Média':^4}')
        for i in range(0, len(lista)):
            print(f'{i:^5}{lista[i][0]:<20}{lista[i][2]:^4}')
        print('-' *30)
        al = int(input('Mostrar nota de qual aluno? (999 para interromper) '))
        while al != 999:
            print(f'Notas de {lista[al][0]} são {lista[al][1][0]} e {lista[al][1][1]}')
            al = int(input('Mostrar nota de qual aluno? (999 para interromper) '))
        print('Finalizando...')
        print('Passar bem. ')
        break