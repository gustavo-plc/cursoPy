l = int(input('Digite a largura da parede a ser pintada: '))
a = int(input('Digite a altura da parede a ser pintada: '))

ar = l * a

print('Você precisará de {:.1f} litros de tinta para pintar essa parede!'.format(ar//2))