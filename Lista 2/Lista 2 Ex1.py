'''1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível o usuário obterá com esses valores.'''

litros = float(input('Digite o valor do litro: '))
dinheiro = float(input('Digite quanto vai pagar: '))

total = dinheiro/litros

print('A quantidade de litros será: {}L'.format(total))
