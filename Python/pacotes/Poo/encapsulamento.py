class BancoDeDados:
    def __init__(self):
        self.__bd = {}
    def incluir_clientes(self,id,nome):
        if 'clientes' not in self.__bd:
            self.__bd['clientes']={id:nome}
        else:
            self.__bd['clientes'].update({id:nome})

dados=BancoDeDados()

dados.incluir_clientes(1,'maria')
dados.incluir_clientes(2,'joao')
dados.__bd='outra coisa'

print(dados.__bd)

print(dados._BancoDeDados__bd)
