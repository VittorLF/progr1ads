'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
'''

a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))

def lados():

    if a > (b + c) or b > (a + c) or c > (a + b):

        print('-=-'*20)
        print('Não é um triângulo ')
        print('-=-'*20)
        exit()

    else:
        print('-=-'*20)
        print('É um triângulo ')
        print('-=-'*20)

lados()

def definir():

    if a == b and a == c and b == c :
        print('-=-'*20)
        print('É um triângulo equilátero ')
        print('-=-'*20)

    elif a == b or a == c or b == c:
        print('-=-'*20)
        print('É um triângulo isósceles ')
        print('-=-'*20)

    else:
        print('-=-'*20)
        print('É um triângulo escaleno ')
        print('-=-'*20)

definir()







