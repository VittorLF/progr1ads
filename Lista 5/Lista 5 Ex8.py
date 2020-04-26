'''8 - Faça um programa que leia 5 números e informe a soma e a média dos números.'''

soma = 0
cont = 0

while cont < 5:
    valor = float(input('Digite o valor: '))
    soma += valor
    cont += 1

media = soma / cont

print('Resultado da soma é: {}'.format(soma))
print('Resultado da média é: {}'.format(media))
