import math

a1 = int(input('Escreva um ângulo em graus: '))

a = math.radians(a1)

print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(a), math.cos(a), math.tan(a)))