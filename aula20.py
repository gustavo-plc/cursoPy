#funções

def soma(a, b):
    s = a + b
    print(s)

def soma1(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é {s}')


#programa principal
a = 4
b = 5
s = a + b

print(s)

a = 8
b = 9
s = a + b

print(s)

a = 2
b = 1
s = a + b

print(s)

#usando a função soma
soma(4, 5)
soma(8, 9)
soma(a=2, b=1) #pode explicitar, e até trocar a ordem, se explicitado

soma1(b=4, a=5)

#empacotamento de parâmetros

def contador(*num): #a fç pode receber vários parâmetros
    tam = len(num)
    print(f'Recebi o valor {num} e são ao todo {tam} números. ')
#cria tupla que recebe os valores para resolver isso...

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


#funções trabalhando com listas

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)