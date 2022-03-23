#'''Exercicio 22 Leia um nome e responda:
# Nome todo em maiusculas
# nome todo em minusculas
# quantas letras possui
# quantas letras tem o primeiro nome
nome = str(input('Qual é seu Nome completo?')).strip()
print('seu nome em maiusculo é {}'.format((nome.upper())))
print(nome.lower())
separado=nome.split()
print(len(nome)-nome.count(' '))
print(len(separado[0]))

#exercicio 23 - leia um número 0 a 9999e responda a quantia em unidade dezena centena e milhar

n=int(input("Escolha um número"))
print("{} tem: \n{} milhares\n{} centenas\n{} dezenas\n{} unidades".format(n,n//1000%10,n//100%10,n//10%10,n//1%10))

#24 - lei a cidade que nasceu e responda se começa com santo

cit=str(input("Em que cidade você nasceu?")).strip()
print(cit[:5].upper() == 'SANTO')

#25 - responder se o nome contem silva

print('seu nome tem silva?{}'.format('silva' in nome.lower()))

#26 - digite uma frase e responda quantas vezez aparece a, sua primeira posição e a ultima posição

fr=str(input('escreva uma frase')).lower().strip()
print('a frase possui {} letras a'.format(fr.count('a')))
print('a primeira posição é {}'.format(fr.find('a')+1))
print('a ultima posição é {}'.format(fr.rfind('a')+1))

#27 - leia o nome, comprimente e responda o primeiro e o ultimo nome
nome1=str(nome.split())
print('muito prazer! Seu primeiro nome é {}'.format(nome1[0]))
print(f'Seu ultimo nome é{nome1[len(nome1)] - 1}')