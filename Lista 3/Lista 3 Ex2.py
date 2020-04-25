'2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'
import time
def função():

    num = float(input('Digite o valor desejado: '))

    if num < 0:
        print('O valor é negativo.')
        função()

    elif num > 0:
        print('O valor é porsitivo.')
        função()

    elif num == 0:
        print('O valor é nulo.')
        função()

função()