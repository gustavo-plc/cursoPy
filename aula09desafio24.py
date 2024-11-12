c = input('Digite o nome de uma cidade: ').strip() # o strip elimina os espaços antes e depois da string

d = c.split()

print(d[0])
print('O primeiro nome é {}'.format(d[0]))
print(d[0].lower().strip() == "santo")

