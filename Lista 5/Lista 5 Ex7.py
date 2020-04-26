'''7 - Faça um programa que leia 5 números e informe o maior número.'''

cont = 1
maior = -999999

while cont < 6:
    valor1 = float(input('Digite o valor: '))
    if valor1 > maior:
        maior = valor1
    cont += 1

print('\nValor maior é: {}'.format(maior))
