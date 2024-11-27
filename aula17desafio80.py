lista = []

for i in range(0, 5): #iterações para adicionar os 5 valores
    dado = int(input('Digite um valor: '))
    if i == 0 or dado > lista[-1]: #se a inserção for a primeira ou se o valor é maior que o último
        lista.append(dado)
    else: # se não for uma inserção no início ou no fim, dada pelo contador i, será no meio
        pos = 0 #definição de um segundo contador
        while pos < len(lista): #enquanto o contador secundário for menor que o tamanho atual da lista: (0, 1, 2, 3, 4)
            if dado <= lista[pos]:
                lista.insert(pos, dado)
                break
            pos += 1

print('A lista na ordem é: ', end = '')
print(lista)
