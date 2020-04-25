# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

def função():

    num1 = float(input('Digite o 1° Número: '))
    num2 = float(input('Digite o 2° Número: '))
    num3 = float(input('Digite o 3° Número: '))

    if num1 < num2 and num1 < num3:
        print('> {}'.format(num1))

        if num2 < num3:
            print('> {}'.format(num2))
            print('> {}'.format(num3))

        else:
            print('> {}'.format(num3))
            print('> {}'.format(num2))

    elif num2 < num1 and num2 < num3:
        print('> {}'.format(num2))

        if num1 < num3:
            print('> {}'.format(num1))
            print('> {}'.format(num3))

        else:
            print('> {}'.format(num3))
            print('> {}'.format(num1))

    else:
        print('> {}'.format(num3))

        if num1 < num2:
            print('> {}'.format(num1))
            print('> {}'.format(num2))

        else:
            print('> {}'.format(num2))
            print('> {}'.format(num1))

função()