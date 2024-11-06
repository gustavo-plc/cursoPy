import math  # importanto a biblioteca toda
from math import ceil
from math import sqrt  # importanto diretamente a função específica

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é {}!'.format(num, ceil(raiz)))
print('A raiz de {} é {}!'.format(num, math.floor(raiz)))
print('A raiz de {} é {:.2f}!'.format(num, raiz))

#para verificar as bibliotecas disponíveis: python.org
#https://docs.python.org/3/library/index.html

import random
numb = random.random() #méthodo random da classe random
numb1 = random.randint(1,10) #méthodo randint da classe random


print(numb)
print(numb1)

#importação de bibliotecas usando pyCharm
#https://pypi.org/project/emoji/

import emoji

print(emoji.emojize('Olá mundo! 😃'))

#a expressão "módulo" é similar a bibliotecas

# qual a diferença entre módulos, pacotes e bibliotecas?

