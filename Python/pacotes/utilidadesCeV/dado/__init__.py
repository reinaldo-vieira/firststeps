def leiamoney():

    while True:
        d = str(input('Insert a value:R$')).strip().replace(',','.')
        if d.isnumeric():
            break
        else:
            print('\033[0;31mError!This value is not compatible.Try again!\033[m')
    return print(f'R${float(d):.2f}'.replace('.',','))


def leiaDinheiro(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'\033[0;31mErro:\"{entrada}\" é um valor inválido!\033[m')
        else:
            valido= True
            return float(entrada)

def leiaint(msg='Insira um número Inteiro'):
    while True:
        try:
            a = int(input(msg))
        except:
            print('\033[0;31mErro!Esse valor não é válido,tente novamente!\033[m')
        else:
            return a
        finally:
            print('\033[4;40mFIM DE PROGRAMA\033[m')


def leiafloat():
    while True:
        try:
            a = float(input('Insira um número real'))
        except:
            print('\033[0;31mErro!Esse valor não é válido\033[m')
        else:
            return a
def siteon(msg):
    import urllib.request
    site=msg
    try:
        site = urllib.request.urlopen(site)
    except:
        print('O site está ta Off')
    else:
        print('O site está On')
        print(site.read())


