expressao = str(input('Digite uma expressão: ')).lower().strip()
expressao_lista = []

for i in range(0, len(expressao)):
    expressao_lista.append(expressao[i])
cont = 0
for i in range(0, len(expressao)):
    if expressao_lista[i] == '(' or expressao_lista[i] == ')':
        cont += 1

print('Sua expressão está correta!' if cont % 2 == 0 else 'Sua expressão está errada!')

