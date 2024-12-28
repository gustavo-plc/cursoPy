def leiaDinheiro(msg):
    while True:
        vlr = str(input(msg))
        while vlr == '' or vlr.isspace() or vlr.isalpha():
            print(f'Erro! {vlr.strip()} é um preço inválido!')
            vlr = str(input(msg))
        if vlr.count(',') == 1:
            vlr = vlr.replace(',', '.')
            vlr = float(vlr)
            break
        vlr = float(vlr)
        break
    return vlr
