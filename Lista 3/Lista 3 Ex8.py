# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

def função():

    prod1 = float(input('Digite o 1° Produto: '))
    prod2 = float(input('Digite o 2° Produto: '))
    prod3 = float(input('Digite o 3° Produto: '))

    menor = prod1

    if prod2 < prod1 and prod2 < prod3:
        menor = prod2

    elif prod3 < prod1 and prod3 < prod2:
        menor = prod3

    print('O produto mais barato dentre os três é o de valor R$ {}'.format(menor))

função()