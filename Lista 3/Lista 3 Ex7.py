#7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

def função():

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    num3 = float(input('Digite o terceiro número: '))

    maior = num1

    if num2 > num1 and num2 > num3:
        maior = num2

    elif num3 > num1 and num3 > num2:
        maior = num3

    menor = num1

    if num2 < num1 and num2 < num3:
        menor = num2

    elif num3 < num1 and num3 < num2:
        maior = num3

    print('O maior número foi {}, e o menor foi {}'.format(maior, menor))

função()