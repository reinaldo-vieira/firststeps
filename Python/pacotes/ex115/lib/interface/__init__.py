def leiaint(msg='Insira um número Inteiro'):
    while True:
        try:
            a = int(input(msg))
        except:
            print('\033[0;31mErro!Esse valor não é válido,tente novamente!\033[m')
        else:
            return a


def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[0;34m{c}\033[m - \033[0;36m{item}\033[m')
        c+=1
    print(linha())
    opc=leiaint('\033[0;37mSua opção\033[m')
    return opc