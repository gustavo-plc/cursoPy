frase = input('Escreva uma frase: ').strip()

print('A letra "A" aparece {} vezes'.format(frase.upper().count('A')))
print('A letra "A" aparece a primeira vez na posição: {} '.format(frase.upper().find('A')+1))
print('A letra "A" aparece a última vez na posição: {} '.format(frase.upper().rfind('A')+1)) #rfind() função começa a procurar pelo lado direito
