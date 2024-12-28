def aumentar(v, p = 0, format = False):
    """
    -> Essa função recebe um valor v e o aumenta em p porcento.
    :param format: se Falso, resultado é número, se True, resultado sai formatado em moeda: "R$ "
    :param v: valor base para aplicação da porcentagem p
    :param p: valor do percentual de aumento a ser aplicado
    :return: o valor final após o aumento
    """
    if format == True:
        return f'R$ {v + p * v / 100}'
    return v + p * v / 100

def diminuir(v, p = 0, format = False):
    """
    -> Essa função recebe um valor v e o reduz em p porcento.
    :param format: se Falso, resultado é número, se True, resultado sai formatado em moeda: "R$ "
    :param v: valor base para aplicação da porcentagem p
    :param p: valor do percentual de redução a ser aplicado
    :return: o valor final após a redução
    """
    if format == True:
        return f'R$ {v - p * v / 100}'
    return v - p * v / 100


def dobro(v, format = False):
    if format == True:
        return f'R$ {2 * v}'
    return 2 * v

def metade(v, format = False):
    if format == True:
        return f'R$ {v / 2}'
    return v / 2

def moeda(v):
    return f'R$ {v}'