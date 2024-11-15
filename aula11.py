print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[97mOlá, Mundo!\033[m')
print('\033[7;97mOlá, Mundo!\033[m') #o 7 inverte o fundo com a fonte

a = 3
b = 5

print('Os valores são \033[1;30;45m{}\033[m e \033[1;34;107m{}\033[m'.format(a, b)) #\033[m

nome = 'Gustavo'
print('Olá, muito prazer em te conhecer, {}{}{}'.format('\033[30;45m', nome, '\033[m')) #utilizando as cores dentro do format!!

cores = {'limpa':'\033[m',          #cores usando dicionário
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto e branco': '\033[7;97m'}

print('Olá, muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa'])) #utilizando as cores dentro do format!!
print('Olá, muito prazer em te conhecer, {}{}{}'.format(cores['azul'], nome, cores['limpa'])) #utilizando as cores dentro do format!!
print('Olá, muito prazer em te conhecer, {}{}{}'.format(cores['preto e branco'], nome, cores['limpa'])) #utilizando as cores dentro do format!!



