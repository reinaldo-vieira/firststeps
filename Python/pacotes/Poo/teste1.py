class Controlador:
    def ligar(self):
        pass

    def desligar(self):
        pass

    def abrirmenu(self):
        pass

    def fecharmenu(self):
        pass

    def maisvolume(self):
        pass

    def menosvolume(self):
        pass

    def ligarmudo(self):
        pass

    def desligarmudo(self):
        pass

    def play(self):
        pass

    def pause(self):
        pass

from interface import Controlador


class Controleremoto(Controlador):
    def __init__(self):
        self.__volume = 50
        self.__tocando = False
        self.__ligado = False

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, v):
        self.__volume = v

    @property
    def tocando(self):
        return self.__tocando

    @tocando.setter
    def tocando(self, t):
        self.__tocando = t

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self, a):
        self.__ligado = a
