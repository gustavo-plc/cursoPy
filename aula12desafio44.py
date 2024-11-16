pr = int(input('Informe o preço do produto: \n'))
con = int(input('Informe a condição de pagamento: \n1- À vista (dinheiro/cheque)\n2- À vista no cartão\n3- Em 2x no cartão\n4- Em 3x ou mais no cartão\n '))

if con == 1:
    print('O valor a ser pago pelo produto será de R$ {:.2f}'.format(pr*0.9))
elif con == 2:
    print('O valor a ser pago pelo produto será de R$ {:.2f}'.format(pr * 0.95))
elif con == 3:
    print('O valor a ser pago pelo produto será de R$ {:.2f}, sendo 2 parcelas de R$ {:.2f} cada'.format(pr,pr/2))
elif con == 4:
    print('O valor a ser pago pelo produto será de R$ {:.2f}'.format(pr * 1.2))