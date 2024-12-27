# ========================
# Definições de cores
# ========================

# Cores

c = ('\033[m',          #0 - sem cores
     '\033[0;30;41m'    #1 - vermelho
     '\033[0;30;42m'    #2 - verde
     '\033[0;30;43m'    #3 - amarelo
     '\033[0;30;44m'    #4 - azul
     '\033[0;30;45m'    #5 - roxo
     '\033[7;30m'       #6 - branco
)


from time import sleep

def escrevaFrosa(msg):
    print('\033[4;30;45m~\033[m' * (len(msg) + 4))
    print(f'{f'\033[4;30;45m{msg:^{(len(msg) + 4)}}\033[m'}')
    print('\033[4;30;45m~\033[m' * (len(msg) + 4))

def escrevaFamar(msg):
    print('\033[4;30;43m~\033[m' * (len(msg) + 4))
    print(f'{f'\033[4;30;43m{msg:^{(len(msg) + 4)}}\033[m'}')
    print('\033[4;30;43m~\033[m' * (len(msg) + 4))

def escrevaAjuda(msg):
    print('\033[0;30;42m ', end='')
    help(msg)
    print('\033[0;30m ', end='')



while True:
    escrevaFrosa('SISTEMA DE AJUDA PYHELP')
    helpi = str(input('Função ou biblioteca: ')).strip().lower()
    if helpi == 'fim':
        break
    else:
        escrevaFamar(f'Acessando o manual do comando {f'<{helpi}>'}')
        sleep(0.5)
        escrevaAjuda(helpi)
        sleep(2)


