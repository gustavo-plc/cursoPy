
def fatorial(n, show = False):
    """

    :param n: o número para o qual se deseja calcular o fatorial
    :param show: se o usuário quer ver a linha das multiplicações
    :return: retorna o valor fatorial do número n
    """
    f = 1

    for c in range(n , 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f


print(fatorial(8, show = True)) #está printando o retorno, ou seja, somente o f

print(fatorial(6)) #está printando o retorno, ou seja, somente o f