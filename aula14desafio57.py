sexo = str(input('Digite o sexo (M/F): \n').lower())

while sexo not in ('m', 'f'):
    print('Opção incorreta, tente novamente digitando M ou F. ')
    sexo = input('Digite o sexo (M/F): \n').lower()
print('Sexo registrado! ')