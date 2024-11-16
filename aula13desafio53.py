frase = input('Escreva uma frase\n').strip().replace(' ','').lower()

c = 0
for i in range(0, len(frase) // 2):
    if frase[i] == frase[len(frase)-1-i]:
        c += 1 #incrementa contador
if c == (len(frase) // 2):
    print('Palíndromo!')
else:
    print('Não palíndromo')