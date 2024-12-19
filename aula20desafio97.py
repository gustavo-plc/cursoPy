def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'{msg:^{(len(msg) + 4)}}')
    print('~' * (len(msg) + 4))


escreva('Olá mundo!')
escreva('Curso em Python no youtube pra galera!')
escreva('CeV')