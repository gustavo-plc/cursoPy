lista = []
while True: #loop infinito de inserção de valores que será quebrado com o break
    lista.append(int(input('Digite um valor: ')))
    mais = str(input('Deseja digitar mais valores? (S/N)').lower().strip())
    while mais not in ('s', 'n'): #se a resposta não estiver dentro desse conjunto...
        print('Formato inválido! \n')
        mais = str(input('Deseja digitar mais valores? (S/N)').lower().strip())
    if mais == 'n':
        break #usado para sair do loop while e finalizar o programa
print(f'Foram digitados {len(lista)} números')
print(f'A lista ordenada de forma decrescente é: {sorted(lista, reverse = True)}')
print(f'A lista contém o valor 5' if lista.count(5) == True else 'Não existe o valor 5 na lista!')
