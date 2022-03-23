from random import randint


class ContaBanco:
    def __init__(self, dono):
        self.numconta = randint(1, 1000)
        self._tipo = None
        self.__status = False
        self.__dono = dono
        self.__saldo = 0

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def abrir_conta(self, tipo):
        if self.status is False:
            self.status = True
        self.tipo = tipo
        if tipo == 'cc':
            self.saldo = 50
        elif tipo == 'cp':
            self.saldo = 150

        print('Sua conta foi aberta')

    def fechar_conta(self):
        if self.status is False:
            print('A conta já se encontra fechada')
        else:
            if self.saldo == 0:
                self.status = False
                print('Sua conta foi fechada')
            elif self.saldo < 0:
                print(f'Seu saldo é negativo.'
                      f'Você precisa depositar R${self.saldo:.2f} para poder fechar a conta')
            elif self.saldo > 0:
                self.saque(self.saldo)
                print(f'Saldo zerado.')
                self.status = False
                print('Sua conta foi fechada.')

    def pagar_mensalidade(self):
        if self.tipo == 'cc':
            self.saldo -= 12
        elif self.tipo == 'cp':
            self.saldo -= 20

        print('Mensalidade paga')

    def deposito(self, valor):
        if self.status is True:
            self.saldo += valor
            print(f'Você depositou R${valor:.2f}')
        else:
            print('Você não pode depositar com a conta fechada')

    def saque(self, valor):
        if self.status is True:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Você sacou R${valor:.2f}')
            else:
                print(f'Você não pode sacar R${valor:.2f}, pois seu saldo é inferior.')
        else:
            print('Você não pode sacar com a conta fechada')

    def saldo_(self):
        print(f'O saldo de {self.dono} é de R${self.saldo:.2f}')

    def estado_atual(self):
        print(f'''
        Numero da conta = {self.numconta}
        Dono = {self.dono}
        Status = {self.status}
        Tipo = {self.tipo}
        Saldo = {self.saldo}''')


c1 = ContaBanco('zeca')
c1.saque(10)
c1.deposito(20)
c1.abrir_conta('cp')
c1.estado_atual()
c1.saldo_()
c1.pagar_mensalidade()
c1.saldo_()
c1.deposito(30)
c1.saldo_()
c1.saque(160)
c1.pagar_mensalidade()
c1.deposito(25)
c1.saldo_()
c1.fechar_conta()
c1.saque(10)
c1.deposito(20)
c1.estado_atual()