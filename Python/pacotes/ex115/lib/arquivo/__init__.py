from ex115.lib.interface import *

def arquivoexiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro!')
    else:
        print('arqivo criado')

def leiaarquiv(nome):
    try:
        a=open(nome,'rt')
    except:
        print(f'Erro ao ler arquivo')
    else:
        cabeçalho('Pessoas cadastradas')

        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(a,b='desconhcido',c=0):
    try:
        a=open(a,'at')
    except:
        print('Houve um erro')
    else:
        try:
            a.write(f'{b};{c}\n')
        except:
            print('Erros nos dados')
        else:
            print('Novo registro')
            a.close()
