'1 - Faça um Programa que peça dois números e imprima o maior deles.'

def função():
    num1 = float(input('Insira o 1° número: '))
    num2 = float(input('Insira o 2° número: '))

    if num1 > num2:
        print('O maior entre eles é {}'.format(num1))

    elif num1 == num2:
        print('Os valores são iguais, digite novamente.\n')
        função()

    else:
        print('O maior entre eles é {}'.format(num2))

função()