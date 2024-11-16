idade_acumulada = 0
maior_idade = 0
mais_velho = ''
mulheres_menos_20 = 0
for i in range(0, 4):
    id = int(input('{}ª pessoa, escreva sua idade:\n'.format(i+1)))
    idade_acumulada += id
    nome = input('Digite seu nome:\n')
    sexo = input('Digite o sexo: (M/F)\n').lower()
    if id > maior_idade and sexo == 'm':
        mais_velho = nome
        maior_idade = id
    if sexo == 'f' and id < 20:
        mulheres_menos_20 += 1

print('A média da idade das pessoas é de {:.2f} anos'.format(idade_acumulada/4))
print('O nome do homem mais velho é {}'.format(mais_velho))
print('{} mulheres tem menos de 20 anos.'.format(mulheres_menos_20))
