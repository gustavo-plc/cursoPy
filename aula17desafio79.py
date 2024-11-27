lista = list()
while True:
    dado = int(input('Digite um valor: '))
    if dado not in lista: #caso seja um valor inédito
        lista.append(dado)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não adicionado! ')

    #verificação de continuidade
    cont = str(input('Deseja continuar? (S/N)')).strip().lower()
    while cont not in {'s', 'n'}:
        print('Dado inválido!')
        cont = str(input('Deseja continuar? (S/N)')).strip().lower()
    if cont == 'n':
        print('#' * 50)
        print(f'Você digitou os valores: {sorted(lista)}') #sorted(lista) não altera a lista, já o lista.sort() altera a original!
        break #sai do laço infinito do while True