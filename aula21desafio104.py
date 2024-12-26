def leiaint(n):
    num = input(n).strip()
    while num.isnumeric() == False:
        print(f'{'\033[0;31mERRO! Digite um número inteiro válido!\033[m'}')
        num = input(n).strip()
    return num


#programa principal

n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
