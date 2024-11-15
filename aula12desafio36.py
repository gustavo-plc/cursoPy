vlr = float(input('Qual é o valor da casa?'))
sal = float(input('Qual o salário?'))
anos = int(input('Em quantos anos deseja pagar?'))

prest = vlr/(anos*12)

if prest <= 0.3*sal:
    print('O valor da prestação mensal é de R$ {:.2f}'.format(prest))
else:
    print('Emprestimo negado!')