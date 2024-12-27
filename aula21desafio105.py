def notas(*n, sit = False): #empacotamento de variáveis: quando não se sabe quantas notas serão passadas
    """
    Função que gera um dicionário a partir das notas informadas, com informações sobre a quantidade de notas, a maior nota,
     a menor nota, a média das notas, e ainda a situação do aluno com base na média.
    :param n: empacotamento das notas a serem passadas. As notas, ao serem passadas, são alocadas em forma de tupla
    :param sit: situação do aluno com base na média de suas notas. Assume valores Razoável, boa e ruim.
    :return: retorna o dicionário com as informações sobre as  notas.
    OBS.: Caso o usuário não passe a opção pela situação, o padrão é não informar, ou seja, false.
    """
    info = dict()
    info['Total'] = len(n)
    info['Maior'] = max(n)
    info['Menor'] = min(n)
    info['Média'] = sum(n)/len(n)
    if sit == False:
        return info
    else:
        if info['Média'] >= 7:
            info['Situação'] = 'Boa'
        elif info['Média'] < 5:
            info['Situação'] = 'Ruim'
        else:
            info['Situação'] = 'Razoável'
        return info

#PROGRAMA PRINCIPAL

resp = notas(1.5, 1, 10, 6.5, sit = True) #passagem de várias notas ao programa e da opção da situação
print(resp)
print()
resp = notas(1.5, 1, 10, 6.5) #passagem de várias notas ao programa e da opção da situação
print(resp)
