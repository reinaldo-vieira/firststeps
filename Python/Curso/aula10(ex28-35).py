#28-o programa deve pensar em um numero entre 0 e 5 e peça pro usuario tentar adiviar qual
# numero foi escolido, após isso deve se dizer se acertou ou não
import random

y=random.randint(0,5)
x=int(input('Adivinhe o número que escolhi(De o a 5)'))
if x==y:
    print('Parabéns! Você acertou, o número oculto era {}'.format(y))
else:
    print('Não foi dessa vez, o número oculto era {}'.format(y))

#29-leia a velocidade de um carro e caso ultrapasse 80km/h mostre uma mensagem dizendo que foi multado
#a multa custa 7,00 por km acima do limite
vel=int(input('Qual é a velocidade do carro?'))
if vel<=80:
    print('Velocidade OK!Pode seguir')
else:
    print('Você excedeu o limite de velicidade em {}km/h, sera multado em R${:.2f}'.format(vel-80,(vel-80)*7))

#30- leia um numero inteiro e mostre se é par ou impar

a=int(input('Digite um número'))
if a%2 == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')

#31- leia a distancia de uma viagem em km e cobre 0,50 por km até 200km,acima disso 0,45

km=float(input("Qual é a distancia da viagem?"))
if km<=200:
    print('O valor da viagem será R${:.2f}'.format(km*0.50))
else:
    print('O valor da viagem será R${:.2f}'.format(km * 0.45))

#32-leia um ano qualquer e mostre se ele é bissexto

from datetime import date

ano=int(input("Escolha uma ano(Digite 0 para selecionar o ano atual)"))
if ano ==0:
    ano = date.today().year

if ano%4==0 and ano % 100 != 0 or ano % 400==0:
    print('Esse ano é Bissexto')
else:
    print('Esse ano não é Bissexto')

#33-leia 3 números e mostre o maior e o menor

b=int(input('Primeiro número'))
c=int(input('Segundo número'))
d=int(input('Terceiro número'))
print('Entre as opções {} é a maior e {} é a menor'.format(max([b,c,d]),min([b,c,d])))

#34- leia o salario e calcule um almento, >1250 10% <1250 15%

sal=float(input('Qual o valor do salário inicial?R$'))
if sal>1250:
    print('O novo salário será de R${:.2f}'.format(sal*1.1))
else:
    print('O novo salário será de R${:.2f}'.format(sal * 1.15))
#35 - lei o comprimento de 3 retas e responda se pode formar um triangulo

l1=int(input('Primeira reta'))
l2=int(input('Segunda reta'))
l3=int(input('Terceira reta'))
if max([l1,l2,l3])<((l1+l2+l3)-max([l1,l2,l3])):
    print('Essas retas formam um triangulo')
else:
    print('Essas retas não formam um triangulo')
    # if l1<l2+l3 and l2<l1+l3 and l3<l1+l2  (também funciona desta forma)
