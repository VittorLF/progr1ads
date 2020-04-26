#5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

pais_a = int(input('Digite a população atual do país A: '))
pais_b = int(input('Digite a população atual do páis B: '))
aumento_a = float(input('Digite quandos % cresce a população do país A anualmente: '))
aumento_b = float(input('Digite quandos % cresce a população do país B anualmente: '))
anos = 0

while pais_a < pais_b:
    pais_a += pais_a * (aumento_a/100)
    pais_b += pais_b * (aumento_b/100)
    anos += 1

print('São nescessários {} anos para o país A ultrapassar o país B'.format(anos))
