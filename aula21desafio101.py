from datetime import datetime

def voto(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade


an = int(input('Em que ano você nasceu? '))
vt = voto(an)

if vt >= 18:
    print(f'Com {vt} anos, o voto é Obrigatório!')
elif vt < 16:
    print(f'Com {vt} anos, o voto é negado!')
else:
    print(f'Com {vt} anos, o voto é Opcional!')