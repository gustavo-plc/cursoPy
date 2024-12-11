lista = []
while True: #loop infinito de inserção de valores que será quebrado com o break
    lista.append(int(input('Digite um valor: ')))
    mais = str(input('Deseja digitar mais valores? (S/N)').lower().strip())
    while mais not in ('s', 'n'): #se a resposta não estiver dentro desse conjunto...
        print('Formato inválido! \n')
        mais = str(input('Deseja digitar mais valores? (S/N)').lower().strip())
    if mais == 'n':
        lista_par = []
        lista_impar = []
        for i in range(0, len(lista)):
            if lista[i] % 2 == 0:
                lista_par.append(lista[i])
            else:
                lista_impar.append(lista[i])
        break #usado para sair do loop while e finalizar o programa
print(f'A lista completa é: {lista}')
print(f'A lista par é: {lista_par}')
print(f'A lista impar é: {lista_impar}')
