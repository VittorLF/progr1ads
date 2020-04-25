'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import math

print('-=-'*20)
a = float(input('Digite o valor de A: '))
print('-=-'*20)
b = float(input('Digite o valor de B: '))
print('-=-'*20)
c = float(input('Digite o valor de C: '))
print('-=-'*20)

if a == 0:
    print('-=-'*20)
    print('A equação não é do segundo grau!!')
    print('-=-' * 20)
    exit()

def delta():

    delta = b*b - (4*a*c)

    if delta < 0:
        print('-=-' * 20)
        print('A equação não possui raízes reais!!')
        print('-=-' * 20)
        exit()

    elif delta == 0:

        raiz = -b / 2*a

        print('-=-' * 20)
        print('Delta tem o valor 0, a equação apresenta apenas uma raiz, sendo essa {:.2f}'.format(raiz))
        print('-=-' * 20)

    else:

        raiz1 = (-b + math.sqrt(delta)) / 2*a
        raiz2 = (-b - math.sqrt(delta)) / 2*a

        print('Raiz são respectivamente: [{}] e [{}]'.format(raiz1, raiz2))
        print('-=-' * 20)

delta()


