from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self,alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo=True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo=False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando=True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando=False

    def get_ano_de_nascimento(self):
        return self.ano_atual-self.idade

    @classmethod
    def por_ano_de_nascimento(cls, nome, ano_de_nascimenro):
        idade = cls.ano_atual - ano_de_nascimenro
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


#class BlocoDeNota:
#    def __init__(self,tipodefolha,folhas,altura,largura,pagina,destacavel=True):
#        self.folhas=folhas
#        self.tipodefolha=str(tipodefolha)
#        self.destacavel=destacavel
#        self.altura=altura
#        self.largura=largura
#        self.pagina=int(pagina)

#    def destacar(self):
#        if self.destacavel:
#            self.folhas-1
#            print(f'Folha destacada, agora restam {self.folhas}')
#        if not self.destacavel:
#            print(f'Este bloco não é destacavel')
#            return
#
#    def escrever(self):
#        if self.pagina==0:
#            print('O bloco está fechado, você não pode escrever.')
#            return
#        if self.pagina !=0:
#            print(f'Você está escrevendo na {self.pagina}° página')

#    def abrir(self,pag):
#        if self.pagina == pag:
#            print(f'O bloco já se encontra na {pag}° página.')
#            return
#        if self.pagina != pag:
#            print(f'Abrindo o bloco na {pag}° pagina.')
#            self.pagina==pag
#            return
#    def fechar(self):
#        if self.pagina==0:
#            print(f'O bloco já se encontra fechado.')
#            return
#        if self.pagina != 0:
#            print(f'Fechando o bloco.')
#            self.pagina==0

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))

    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self,valor):
        if isinstance(valor,str):
            valor=float(valor.replace('R$',''))

        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()
class A:
    vc =123

    def __init__(self):
        self.vc = 222
