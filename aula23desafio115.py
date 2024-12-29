# Finally, the last one!

# c = ('\033[m',          #0 - sem cores
#      '\033[0;30;41m'    #1 - vermelho
#      '\033[0;30;42m'    #2 - verde
#      '\033[0;30;43m'    #3 - amarelo
#      '\033[0;30;44m'    #4 - azul
#      '\033[0;30;45m'    #5 - roxo
#      '\033[7;30m'       #6 - branco
# )

from time import sleep


def mostraMenu():
    print('--' *30)
    print(f'{'MENU PRINCIPAL':^60}')
    print('--' *30)
    print('\033[1;33m1\033[m - ', end = '')
    print('\033[1;35mVer pessoas cadastradas\033[m')
    print('\033[1;33m2\033[m - ', end = '')
    print('\033[1;35mCadastrar nova pessoa\033[m')
    print('\033[1;33m3\033[m - ', end = '')
    print('\033[1;35mSair do sistema\033[m')
    print('--' *30)
    while True:
        try:
            op = int(input('\033[1;36mSua opção:\033[m ').strip())
        except ValueError:
            print('Digite uma opção válida')
        except TypeError:
            print('Digite uma opção válida')
        except KeyboardInterrupt:
            print('Cancelado pelo usuário')
            break
        except Exception as erro:
            print(f'Erro indefinido: {erro}')
        else:
            while op not in {1, 2, 3}:
                print('Digite um número válido')
                op = int(input('\033[1;36mSua opção:\033[m ').strip())
            global nome_ar
            nome_ar = 'cadastro.txt'
            if op == 1:
                mostraPessoas()
            if op == 2:
                cadastraPessoas()
            if op == 3:
                print('Atualizando informações...')
                for i in range (0, 10):
                    print('.', end = '')
                    sleep(0.3)
                print('.')
                print(F'{'PROGRAMA ENCERRADO':^60}')

                break
        break

def mostraPessoas():
    print('--' * 30)
    print(f'{'PESSOAS CADASTRADAS':^60}')
    print('--' * 30)
    conteudo = leArquivo(nome_ar)
    printaArquivo(conteudo)
    mostraMenu()

def leArquivo(nome_ar):
    try:
        with open(nome_ar, 'r') as arquivo:
            conteudo = arquivo.read()
            if conteudo == '':
                print(f'Nenhuma pessoa cadastrada.')
            else:
                return printaArquivo(conteudo)
    except FileNotFoundError:
        print(f'Não há pessoas cadastradas ou o arquivo não foi encontrado!')
    except PermissionError:
        print(f'Permissão negada para acessar o arquivo {nome_ar}')
    except Exception as erro:
        print(f'Erro inesperado: {erro}')

def printaArquivo(conteudo):
    try:
            print(conteudo)
    except Exception as erro:
        print(f'Erro inesperado: {erro}')

def cadastraPessoas():

    print('--' * 30)
    print(f'{'NOVO CADASTRO':^60}')
    print('--' * 30)
    while True:
        try:
            nomep = str(input('\033[1;34mNome:\033[m ').strip())
        except ValueError:
            print('Digite uma opção válida')
        except TypeError:
            print('Digite uma opção válida')
        except KeyboardInterrupt:
            print('Cancelado pelo usuário')
            break
        except Exception as erro:
            print(f'Erro indefinido: {erro}')
        else:
            while True:
                try:
                    idadep = int(input('\033[1;34mIdade:\033[m ').strip())
                except ValueError:
                    print('Digite uma opção válida')
                except TypeError:
                    print('Digite uma opção válida')
                except KeyboardInterrupt:
                    print('Cancelado pelo usuário')
                    idade = 0
                    break
                except Exception as erro:
                    print(f'Erro indefinido: {erro}')
                else:
                    pessoa = f'{nomep:<25}' + f'{''}'*30 + f'{str(idadep):<5}' + '\n'
                    salvaArquivo(nome_ar, pessoa)
                    break
        break

def salvaArquivo(nome = ' ', conteudo = ''):
    try:
        with open(nome_ar, 'a') as arquivo:
            arquivo.write(conteudo)
        print(f'Conteúdo salvo com sucesso!')
    except PermissionError:
        print(f'Permissão negada para salvar o arquivo {nome_ar}')
    except Exception as erro:
        print(f'Erro inesperado: {erro}')
    else:
        mostraMenu()

mostraMenu()