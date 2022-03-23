class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = CarrinhoDeCompras()
p1 = Produto('camiseta', 30)
p2 = Produto('Bermuda', 50)
p3 = Produto('Tenis', 100)


print(f'O seu carrinho possui:')
carrinho.lista_produto()
print(f'A soma da sua compra é de R${carrinho.soma_total()}')
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
print(f'O seu carrinho possui:')
carrinho.lista_produto()
print(f'A soma da sua compra é de R${carrinho.soma_total()}')
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
print(f'O seu carrinho possui:')
carrinho.lista_produto()
print(f'A soma da sua compra é de R${carrinho.soma_total()}')
