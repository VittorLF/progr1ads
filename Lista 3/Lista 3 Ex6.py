# 6 - Faça um Programa que leia três números e mostre o maior deles.

def função():

    num1 = float(input('Digite o 1° número: '))
    num2 = float(input('Digite o 2° número: '))
    num3 = float(input('Digite o 3° número: '))

    maior = num1

    if num2 > num1 and num2 > num3:
        maior = num2

    elif num3 > num1 and num3 > num2:
        maior = num3

    print('\nO maior número é {}'.format(maior))

função()