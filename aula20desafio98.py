from time import sleep

def contador(i, f, p):
    cont = i  #variável auxiliar que recebe o início
    if i > f: #caso em que o início é maior que o fim, ou seja, contagem regressiva
        while cont >= f: #enquanto a variável que recebeu o início for maior que o final...
            print(f'{cont}', end = ' ') #imprime o auxiliar
            sleep(0.5)
            cont -= p #auxiliar é decrementado do passo, para uma contagem regressiva
        print()
    else: #caso início seja menor que o fim, contagem progressiva
        while cont <= f: #enquanto contagem for menor que o fim
            print(f'{cont}', end = ' ') #imprime variável
            sleep(0.5)
            cont += p #incrementa variável com passo, no caso de contagem progressiva
        print()


#programa principal


contador(1, 10, 1)
contador(90, 40, 10)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
