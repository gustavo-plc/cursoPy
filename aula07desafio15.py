k = int(input('Quantos km foram percorridos? '))
d = int(input('Por quantos dias o carro foi alugado? '))

print('O preço a ser pago peço aluguel é de R${:.2f}'.format(60*d+0.15*k))