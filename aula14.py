#ESTRUTURA DE REPETIÇÃO WHILE

for c in range (1,10): #para situações em que sei a quantidade de iterações
    print(c)
print('fim')

i = 1
while i <10: #while serve para situações em que sei o limite de iterações e também para quando não sei
    i += 1
    print(i)
print('fim')

n = 1
while n != 0: #aqui não se sabe o número de iterações, apenas que quando se digitar zero o programa termina.
    n = int(input('Digite um valor: '))
print('fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Quer cntinuar? (S/N) ').upper()
print('Fim')