class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando ...')

# class Cliente:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade


# class Aluno:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando ...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando ...')


p1 = Pessoa('Helio', 40)
p1.falar()
print()
c1 = Cliente('Emanuela', 20)
c1.falar()
c1.comprar()
print()
a1 = Aluno('Fabricio', 28)
a1.falar()
a1.estudar()
