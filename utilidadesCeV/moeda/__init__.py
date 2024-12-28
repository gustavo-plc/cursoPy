
def aumentar(v, p = 0, format = False):
    """
    -> Essa função recebe um valor v e o aumenta em p porcento.
    :param format: se Falso, resultado é número, se True, resultado sai formatado em moeda: "R$ "
    :param v: valor base para aplicação da porcentagem p
    :param p: valor do percentual de aumento a ser aplicado
    :return: o valor final após o aumento
    """
    if format == True:
        return f'R$ {v + p * v / 100:.2f}'
    return f'{v + p * v / 100:.2f}'

def diminuir(v, p = 0, format = False):
    """
    -> Essa função recebe um valor v e o reduz em p porcento.
    :param format: se Falso, resultado é número, se True, resultado sai formatado em moeda: "R$ "
    :param v: valor base para aplicação da porcentagem p
    :param p: valor do percentual de redução a ser aplicado
    :return: o valor final após a redução
    """
    if format == True:
        return f'R$ {v - p * v / 100:.2f}'
    return f'{v - p * v / 100:.2f}'


def dobro(v, format = False):
    if format == True:
        return f'R$ {2 * v:.2f}'
    return f'{2 * v:.2f}'

def metade(v, format = False):
    if format == True:
        return f'R$ {v / 2:.2f}'
    return f'{v / 2:.2f}'

def moeda(v):
    return f'R$ {v:.2f}'

def resumo(v, aumento = 0, reducao = 0):
    print('-' * 50)
    print(f'{'RESUMO DO VALOR':^50}')
    print('-' * 50)
    print(f'{'Preço analisado: ':<30}', end = '')
    print(f'{f'{moeda(v)}':<20}')
    print(f'{'Dobro do preço: ':<30}', end = '')
    print(f'{f'{dobro(v, True)}':<20}')
    print(f'{'Metade do preço: ':<30}', end = '')
    print(f'{f'{metade(v, True)}':<20}')
    print(f'{f'{aumento}% de aumento: ':<30}', end = '')
    print(f'{f'{aumentar(v, aumento, True)}':<20}')
    print(f'{f'{reducao}% de redução: ':<30}', end = '')
    print(f'{f'{diminuir(v, reducao, True)}':<20}')
    print('-' * 50)