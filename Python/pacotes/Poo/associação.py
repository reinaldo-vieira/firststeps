class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__feramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__feramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__feramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('A caneta está escrevendo')


escritor = Escritor('João de Oliveira')
caneta = Caneta('bic')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
print(escritor.nome)
