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
