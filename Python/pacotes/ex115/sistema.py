from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq='cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Criar Arquivo','Cadastrar Pessoas','Sair do Sistema'])
    if resposta==1:
        leiaarquiv(arq)
    elif resposta==2:
        cabeçalho('Novo Cadastro')
        nome=str(input('Nome'))
        idade=leiaint('idade')
        cadastrar(arq,nome,idade)
    elif resposta==3:
        cabeçalho('Saindo do sistema...Até logo!')
        break
    else:
        print('Erro! Digite uma opção válida!')
    sleep(2)
