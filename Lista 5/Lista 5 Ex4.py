# 4 - Suponha que a população de um país A seja da ordem de 80.000 habitantes com umataxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxade crescimento de 1.5%. Faça um programa que calcule e escreva o número de anosnecessários para que a população do país A ultrapasse ou iguale a população do país B,mantidas as taxas de crescimento.

# A cresce 2400 anualmente
# B cresce 3000 anualmente

print('A população atual do país A de 80.000 ')
print('A população atual do país B de 200.000 ')

pais_a = 80000
pais_b = 200000
anos = 0

while pais_a < pais_b:
    pais_a += pais_a * 0.03
    pais_b += pais_b * 0.015
    anos += 1

print('São nescessários {} anos para o país A ultrapassar o país B'.format(anos))
