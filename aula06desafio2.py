n = input('Digite algo: ')

print('O tipo primitivo desse dado é: {}'.format(type(n)))
print('Só tem espaços? ',n.isspace())
print('É um número? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está em maiúsculas? ', n.isupper())
print('Está em minúsculas? ', n.islower())
print('Está capitalizada? ', n.istitle())




