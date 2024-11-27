#tupla é um vetor que aceita qualquer tipo de dados
#tuplas são imutáveis! Uma vez definidos os valores de cada índice
# do vetor, são imutáveis!

#para alterar os índices de cada posição:
#UTILIZA-SE LISTA!!!!

#tuplas: ()
#listas: []

#a principal diferença é que se pode
#alterar os valores de cada índice da lista.

#listas são mutáveis, e possuem vários métodos associados!!

#MÉTODOS
#append('item')
#insert(posição, 'item')
# del lista[posição] - remove pela posição
#lista.pop(posição) - remove pela posição. Sem posição? remove o último
#lanche.remove('item') - remove pelo conteúdo

#para as deleções, elimina-se o conteúdo e refaz-se os índices automaticamente

#ao tentar remover um elemento que não existe: ERRO

#possível criar listas por meio do range

#valores = list(range(4, 11))
# 4 5 6 7 8 9 10

#ordenar valores na lista: valores.sort()
#ordem reversa? sim: valores.sort(reverse = True)
#len também funciona para retornar o tamanho da lista

num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
#é possível alterar a lista!
# num[4] = 7 erro!!

num.append(7) #adicionando o valor 7 ao final
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

print(f'Essa lista tem {len(num)} elementos!')

#adicionando valor na posição x (reposicionamento automático)
num.insert(2, 14)
print(num)

#para remover o último elemento
num.pop()
print(num)

#remove o elemento da posição 2 e reposiciona os demais
num.pop(2)
print(num)

num.insert(2, 2)
print(num)

num.remove(2) #remove a primeira ocorrência do valor
print(num)

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

#criando lista vazia de duas formas:

lista = []
#OU
# lista2 = list()

lista.append(5)
lista.append(9)
lista.append(4)
print(' \n')

for v in lista:
    print(f'{v}...', end = '')

#para apresentar tanto a chave quanto o valor, temos o ENUMERATE:

print('')

for c, v in enumerate(lista):
    print(f'Na posição {c} temos o valor {v}')

lendo = list()

for cont in range (0, 5):
    lendo.append(int(input('Digite um valor para a lista: \n'))) #lendo valores do teclado e inserindo na lista
print(lendo)

#QUESTÃO DA LIGAÇÃO/CÓPIA ENTRE LISTAS

a = [2, 3, 4, 7] #declarei e atribui uma lista
b = a #lista B se liga à lista A (É FEITA UMA LIGAÇÃO ENTRE ELAS, ALTERAR A ALTERA B)!
b[2] = 8 #alterei o valor do elemento da posição 2 da lista b

print(a)
print(b)

#para criar uma CÓPIA, E NÃO LIGAÇÃO:

b = a[:] # b recebe uma cópia de a

b[0] = 1
print('')
print(a)
print(b)

