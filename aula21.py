def somar(a = 0, b = 0, c = 0): #usando parâmetros opcionais: a = 0, b = 0, c = 0

    """ #elaborando docstrings para uma função
    -> Soma os três valores passados e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    """

    s = a + b + c
    print(f'A soma vale {s}')

somar(2, 3, 5)
somar(2, 3)
somar(2)
somar()

#escpopo de variáveis: local e global
print()


#LOCAL

def teste(b):
    a = 8 # a local: declarada dentro da função, tem escopo local. É criado um A local para receber 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#PROGRAMA PRINCIPAL

a = 5 #a global, declarada no programa principal, tem escopo global.
teste(a)
print(f'A fora vale {a}')


print()
#ALTERANDO VARIÁVEL GLOBAL DENTRO DA FUNÇÃO

def teste(b):
    global a
    a = 8 # a local: declarada dentro da função, mas com CHAMADA GLOBAL antes. É alterado o A global para 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#PROGRAMA PRINCIPAL

a = 5 #a global, declarada no programa principal, tem escopo global.
teste(a)
print(f'A fora vale {a}')


print()
# RETORNO DE FUNÇÕES !

def somar(a = 0, b = 0, c = 0): #usando parâmetros opcionais: a = 0, b = 0, c = 0

    s = a + b + c
    return s

resp = somar(2, 3, 5)
print(resp)
print(somar(2, 5, 6))

r1 = somar(1, 2)
r2 = somar(4, 6, 34)
r3 = somar(10, 10, 100)

print(f'Meus resultados foram {r1}, {r2} e {r3}')

print()
# FATORIAL

def fatorial(n = 1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))

print(f'O fatorial de {n} é {fatorial(n)}')