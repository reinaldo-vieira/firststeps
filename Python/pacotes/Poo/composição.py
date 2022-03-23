class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.esado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.esado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.esado} FOI APAGADO')


cliente1 = Cliente('João', '30')
cliente1.inserir_endereco('Joinville', 'SC')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Ana', 20)
cliente2.inserir_endereco('Campinas', 'SP')
cliente2.inserir_endereco('Rezende', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('Dudu', 15)
cliente3.inserir_endereco('Manaus', 'AM')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print('#'*25)

print()
