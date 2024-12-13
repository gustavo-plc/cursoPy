lista_ind = ['', 0]
lista_geral = []
while True: #loop infinito de inserção de valores que será quebrado com o break
    lista_ind[0] = str(input('Digite um nome: ')).strip()
    lista_ind[1] = int(input('Digite o peso: '))
    lista_geral.append(lista_ind[:])
    mais = str(input('Deseja digitar mais valores? (S/N)').lower().strip())
    while mais not in ('s', 'n'): #se a resposta não estiver dentro desse conjunto...
        print('Formato inválido! \n')
        mais = str(input('Deseja digitar mais valores? (S/N)').lower().strip())
    if mais == 'n':
        maior_peso = menor_peso = lista_geral[0][1]
        for i in range(1, len(lista_geral)):
            if lista_geral[i][1] > maior_peso:
                maior_peso = lista_geral[i][1]
            if lista_geral[i][1] < menor_peso:
                menor_peso = lista_geral[i][1]
        print(f'Ao todo foram cadastradas {len(lista_geral)} pessoas.')
        print(f'O maior peso é {maior_peso}.', end=' Peso de ')
        for i in range(len(lista_geral)):
            if lista_geral[i][1] == maior_peso:
                print(f'{lista_geral[i][0]}', end = ' ')
        print(f'\nO menor peso é {menor_peso}.', end=' Peso de ')
        for i in range(len(lista_geral)):
            if lista_geral[i][1] == menor_peso:
                print(f'{lista_geral[i][0]}', end=' ')
        break #usado para sair do loop while e finalizar o programa
