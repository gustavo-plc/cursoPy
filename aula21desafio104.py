def leiaint(n):
    num = input(n).strip()
    while num.isnumeric() == False:
        print(f'{'ERRO! Digite um número inteiro válido!':3}')
        num = input(n).strip()
    return num


#programa principal

n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
