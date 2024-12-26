
def voto(ano_nascimento):
    from datetime import date  # escopo de importação: com essa identação, importa somente para a função.
    #economiza memória

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos, não se vota. '
    elif idade >= 18:
        return f'Com {idade} anos, o voto é obrigatório!'
    else:
        return f'Com {idade} anos, o voto é opcional! '


print(voto(int(input('Em que ano você nasceu? '))))
