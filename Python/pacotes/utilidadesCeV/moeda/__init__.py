def aumentar(val=0,aumento=0,form=False):
    aum=val*(1+(aumento/100))
    if form:
        return moeda(aum)
    else:
        return aum


def diminuir(val=0,reduçao=0,form=False):
    red=val*(1-(reduçao/100))
    if form:
        return moeda(red)
    else:
        return red


def dobro(val=0,form=False):
    vf=val*2
    if form:
        return moeda(vf)
    else:
        return vf



def metade(val=0,form=False):
    vf=val/2
    if form:
        return moeda(vf)
    else:
        return vf


def moeda(p=0):
    return f'R${p:.2f}'.replace('.',',')


def resumo(p=0,aumi=0,redi=0):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado:\t{moeda(p)}')
    print(f'Dobro do Preço:\t\t{dobro(p, True)}')
    print(f'Metade do Preço:\t{(metade(p, True))}')
    print(f'Aumentando {aumi}%:\t\t{(aumentar(p,aumi, True))}')
    print(f'Reduzindo {redi}%:\t\t{(diminuir(p, redi, True))}')
    print('-' * 30)
