nome = input('Digite seu nome completo: ').strip()

nome_lista = nome.split()

print('O primeiro nome é: {}'.format(nome_lista[0]))
print('O último nome é: {}'.format(nome_lista[len(nome_lista)-1]))