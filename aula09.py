frase = '   Curso em Vídeo Python   '

print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[7:])
print(frase[1:15:2]) #início:fim:passo
print(frase[::2]) #início:fim:passo
print("""Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, 
funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. Wikipédia""") #com aspas triplas, o print respeita a quebra de linha colocada pelo usuário

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O')) #combinando funções
print(frase)
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android')) #uso da função replace: possibilidade de alterar a string para visualização. Não muda EFETIVAMENTE, só muda para exibição

#strings são imutáveis em seus microespaços! só é possível alterá-la usando-se uma função de transformação e usando atribuição nela mesma.

print(frase)

frase = frase.replace('Python', 'Android') #alteração da string

print(frase)

print('Curso' in frase)
print(frase.find('Python'))
print(frase.find('Android'))
print(frase.lower().find('android'))

print(frase.split())

dividido = frase.split() #o split gera uma lista

print(dividido[2])
print(dividido[2][3])



