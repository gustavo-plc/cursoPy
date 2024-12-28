def aumentar(v, p = 0):
    """
    -> Essa função recebe um valor v e o aumenta em p porcento.
    :param v: valor base para aplicação da porcentagem p
    :param p: valor do percentual de aumento a ser aplicado
    :return: o valor final após o aumento
    """
    return v + p * v / 100

def diminuir(v, p = 0):
    """
    -> Essa função recebe um valor v e o reduz em p porcento.
    :param v: valor base para aplicação da porcentagem p
    :param p: valor do percentual de redução a ser aplicado
    :return: o valor final após a redução
    """
    return v - p * v / 100


def dobro(v):
    return 2 * v

def metade(v):
    return v / 2