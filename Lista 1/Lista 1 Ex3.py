'''3 - Em um banho de 5 minutos, fechando o registro ao se ensaboar, são gastos 45 litros de água.
Sabendo que em 1 m3 de água há 1.000 litros, calcule quantos banhos de 5 minutos são
necessários para consumir 1 metro cúbico de água?
'''

tempo = float(input('Digite quanto tempo demora o seu banho: '))
litros_mn = 9
total_banho = litros_mn * tempo
total = 1000/total_banho

print('A quantidade de banhos nescessárias para alcançar 1 m³ de água é de: {} banhos'.format(int(total)))


