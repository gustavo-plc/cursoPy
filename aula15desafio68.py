import random

print('*'*30)
print('Par ou Ímpar')
print('*'*30)
vitorias = 0

while True:
    valor = int(input('informe um valor: '))
    escolha = str(input('Você quer par ou ímpar? (P/I)?')).lower()

    #verificação de entrada válida
    while escolha not in {'p', 'i'}:
        print('Escolha inválida. Digite "P" para Par ou "I" para Ímpar.')
        escolha = str(input('Você quer par ou ímpar? (P/I)?')).lower()

    #escolha do computador
    pc = random.randint(1,10) #random.randint inclui os dois extremos
    print(f'O computador escolheu o número {pc}')

    #resultado
    soma = pc + valor
    if soma % 2 == 0:
        resultado = 'p'
    else:
        resultado = 'i'

    #verificação do vencedor
    if (escolha == resultado):
        print(f'Você ganhou! A soma foi {soma}, que é {"Par" if resultado == "p" else "Ímpar"}.')
        vitorias += 1
    else:
        print(f'Você perdeu, porque {soma} é {'par' if resultado == 'p' else 'ímpar'}')
        break

    #fim do jogo
    print(f'Você venceu {vitorias} vezes consecutivas')




















