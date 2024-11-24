#Tupla: uma variável composta que guarda um ou mais valores
#tipo de indexação por índices
#uma string já é uma variável composta, pois cada elemento é acessado por índices

#print(lanche[0:2]) : faz do zero, incluso, até o 2 excluso
#for c in lanche: usando o for com variáveis compostas
#   print(c)

#AS TUPLAS SÃO IMUTÁVEIS: não é possível trocar o valor de cada índice.

#lanche = 'Hamburguer'
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #tupla entre parenteses

print(lanche)
print(lanche[3])
print(lanche[-2])
print(lanche[1:3]) #mostra o [1] e o [2], o 3 não é incluso
print(lanche[2:]) #mostra do [2] até o final
print(lanche[:2]) #mostra do início até o 1 (exclui o 2)
print(lanche[-2:])

#tuplas são imutáveis!

print(lanche[1])
#ERRO!: lanche[1] = 'Refrigerante' não é possível!

print(len(lanche))

for cont in range(0,len(lanche)): #usando range
    print(f'Eu vou comer {lanche[cont]} na posição {cont}!')
#bom quando precisa mostrar a posição
print('\n')

for comida in lanche: #usando diretamente a variável composta
    print(f'Eu vou comer {comida}!')
print('\n')

for pos, comida in enumerate(lanche): #forma de obter posição
#com enumerate
    print(f'Eu vou comer {comida} na posição {pos}!')
print('\n')
print('Comi demais!')

#mét/odo sorted: mostra em ordem alfabética

print(sorted(lanche)) #ordenado em ordem alfabética


#uso de operadores em tupla
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #concatena as tuplas != de b + a
print(a)
print(b)
print(c)
print(len(c))

#mét/odo interno da tupla
print(c.count(5)) #quantas vezes aparece o 5?
print(c.count(4)) #
print(c.count(9))
print(c.index(8)) #em que posição está o 8?
print(c.index(2)) #pega a primeira ocorrência do 2
print(c.index(5, 1)) #pega a primeira ocorrência do 5 a partir da posição 1

pessoa = (1, 2, 3, 4, 5, 'Gustavo', '74.50')
#as tuplas podem armazenar dados de tipos diferentes!

print(pessoa)

#é possível apagar a tupla toda, mas não 1 só elemento
#del(pessoa)



