def leiaDinheiro(msg):
    while True:
        vlr = str(input(msg)).replace(',', '.').strip()
        while vlr == '' or vlr.isalpha():
            print(f'Erro! {vlr.strip()} é um preço inválido!')
            vlr = str(input(msg)).replace(',', '.').strip()
        vlr = float(vlr)
        break
    return vlr
