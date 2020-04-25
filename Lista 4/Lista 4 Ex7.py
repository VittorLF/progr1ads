#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Informe o ano (Ex: 2020), para saber se é Bissexto ou não: '))

def ano_bissexto():

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

        print('-=-' * 10)
        print('É um ano Bissexto')
        print('-=-' * 10)

    else:

        print('-=-' * 10)
        print('Não é um ano Bissexto')
        print('-=-' * 10)

ano_bissexto()
