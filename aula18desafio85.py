lista = list()
lista_par = list()
lista_impar = list()

for i in range(0, 7):
    lista.append(int(input(f'Digite o {i+1}º número: ')))
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

lista.clear()
lista_par.sort()
lista_impar.sort()
lista.append(lista_par)
lista.append(lista_impar)

print(f'Os números pares digitados foram: {lista_par}')
print(f'Os números ímpares digitados foram: {lista_impar}')