import random
jogada = int(input('Digite o número correspondente ao que você quer colocar na jogada!\n1- Pedra\n2- Papel\n3- Tesoura\n'))
jogada_pc = random.randint(1,3)
dic = {1:'Pedra', 2:'Papel', 3:'Tesoura'}

print('Você jogou {}'.format(dic[jogada]))
print('O computador jogou {}'.format(dic[jogada_pc]))


if jogada == jogada_pc:
    print('{} empata com {}!'.format(dic[jogada_pc], dic[jogada]))
elif (jogada == 1 and jogada_pc == 2) or (jogada == 2 and jogada_pc == 3) or (jogada == 3 and jogada_pc == 1):
    print('{} ganha de {}!'.format(dic[jogada_pc], dic[jogada]))
else:
    print('{} ganha de {}!'.format(dic[jogada], dic[jogada_pc]))
