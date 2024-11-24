cont_maior = 0
cont_mulher_menos20 = 0
cont_homens = 0

while True:
    # primeira leitura de idade

    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).lower().strip()

    # tratamento de exceção do sexooo

    while sexo not in {'m', 'f'}:
        print('Entrada inválida. Digite novamente o sexo no formato (M)asculino ou (F)eminino:  ')
        sexo = str(input('Digite o sexo (M/F): ')).lower().strip()

    #contagem de maiores de idade:

    if idade >= 18:
        cont_maior += 1
    if sexo == 'm':
        cont_homens += 1
    if sexo == 'f' and idade <20:
        cont_mulher_menos20 += 1

    #laço externo para saber se o usuário quer continuar

    mais = str(input('Deseja entrar com mais dados?  (S/N)')).lower().strip()
    while mais not in {'s', 'n'}:
        print('Entrada inválida. Digite novamente no formato (S)im ou (N)ão:  ')
        mais = str(input('Deseja entrar com mais dados?  (S/N)')).lower().strip()

    if mais == 'n':
        print('Obrigado por utilizar nosso programa!\n')
        break

print(f'Há {cont_maior} pessoas maiores de idade')
print(f'Há {cont_homens} homen(s)')
print(f'Há {cont_mulher_menos20} mulher(es) com menos de 20 anos')