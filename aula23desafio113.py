def leiaInt(n):
    while True:
        try:
            num = int(input(n).strip())
        except ValueError:
            print('Favor digitar um número inteiro!')
        except KeyboardInterrupt:
            num = -1
            print('\nOperação cancelada pelo usuário!')
            break
        except EOFError:
            print('Entrada inesperada encerrada. Nenhum dado fornecido!')
        except Exception as erro:
            print(f'Erro inesperado {erro.__class__}')
        else:
            break
    return num


def leiaFloat(n):
    while True:
        try:
            num = float(input(n).strip())
        except ValueError:
            print('Favor digitar um número real!')
        except KeyboardInterrupt:
            num = -1
            print('\nOperação cancelada pelo usuário!')
            break
        except EOFError:
            print('Entrada inesperada encerrada. Nenhum dado fornecido!')
        except Exception as erro:
            print(f'Erro inesperado {erro.__class__}')
        else:
            break
    return num


#programa principal

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')


print(f'O número inteiro digitado foi {n1} e o real foi {n2:.2f}')
