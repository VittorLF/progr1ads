'''10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 > valor2:
    cont = valor1
    cont2 = valor2

elif valor2 > valor1:
    cont = valor2
    cont2 = valor1

cont -= 1

while cont2 < cont:
    print(cont)
    cont -= 1
