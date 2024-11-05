n = float(input('Digite um valor: '))
print(n)

#trabalhando com tipo booleano

s = bool(input('Digite um valor: '))
print(s) #se tiver valor na variável, qualquer um, imprime verdadeiro. Caso não tenha, imprime falso.

t = input('Digite algo: ')
print(t.isnumeric()) #esse metodo informa se é possível converter o que foi escrito em um número INTEIRO!

x = input('Digite algo: ')
print(x.isalpha())

y = input('Digite algo: ')
print(y.isalnum())