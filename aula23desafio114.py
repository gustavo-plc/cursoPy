# THE almost LAST CHALLENGE!!!

import urllib.request
import ssl

url = 'https://www.pudim.com.br/'

try:
    context = ssl._create_unverified_context()
    site = urllib.request.urlopen(url, context = context)

except Exception as erro:
    print(f'O site {url} está indisponível no momento. Erro: {erro.__class__}')
else:
    print('Tudo ok! Site disponível!')
