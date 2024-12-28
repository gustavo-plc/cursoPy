# Exceções - Exception
#
# NameError
# ValueError
# ZeroDivisionError
# TypeError
# IndexError
# KeyError
# EOFError
# KeyboardInterrupt
# OSError
# MemoryError
# ConnectionError
# RuntimeError

# try:
#     [comandos que podem dar pau]
# except:
#     [se a coisa de cima falhar, o que acontecerá?]
# except: pode-se ter quantos forem preciso.
# else:
#     [no caso de dar certo]
# finally:
#       [dando certo ou errado, será executado]
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre, muito obrigado')