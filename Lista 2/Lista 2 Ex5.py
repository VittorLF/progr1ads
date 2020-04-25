'''5. Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).'''

valor_divida = float(input('Digite o valor da dívida: '))
dias_de_atraso = int(input('Digite a quantidade de dias atrasados: '))
taxa_diaria = float(input('Digite a multa diária por atraso: '))

total = valor_divida + (dias_de_atraso * taxa_diaria)

print('O valor a ser pago é R${}'.format(total))