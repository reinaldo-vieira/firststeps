from pessoas import Pessoa,Produto,A

p1 = Pessoa('Zeca',27)
p2 = Pessoa('Laura',22)

p2.comer('jilo')
p1.falar('Python')
p2.falar('cobras')
p1.falar('trabalho')
p2.parar_comer()
p2.falar('aulas')
p1.parar_falar()
p1.falar('mouse')
p1.comer('caqui')
p1.parar_falar()
p1.comer('bolacha')
p1.parar_comer()
p1.falar('camisas')
print(p1.ano_atual)
print(p2.ano_atual)

print(p1.get_ano_de_nascimento())
print((p2.get_ano_de_nascimento()))

#(from pessoas import BlocoDeNota

#b1=BlocoDeNota(20,'pautada',15,20,0,True)
#b2=BlocoDeNota(15,"branca",20,30,10,False)

#b1.abrir(2)
#b1.escrever()
#b1.abrir(10)
#print(b1.pagina())
#b1.escrever()
#b1.destacar()
#b1.destacar()
#print(b1.pagina())
#b1.fechar()

print(p1.gera_id())
print(p2.gera_id())

r1 = Produto("camisa",50)
r1.desconto(10)
print(r1.preco)

r2 = Produto('caneca','R$20')
r2.desconto(15)
print(r2.preco)

a1= A()
a2= A()

print(a1.vc)
print(a2.vc)
print(A.vc)

A.vc=321

print(a1.vc)
print(a2.vc)
print(A.vc)

a1.vc=123

print(a1.vc)
print(a2.vc)
print(A.vc)

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
