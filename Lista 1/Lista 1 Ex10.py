'''10 - Escreva um programa que converta valores de centímetros em polegadas.'''

centimentros = float(input('Digite o valor em centimetros: '))

polegadas = centimentros/2.54

print('{} centimetros é {:.2f} polegadas'.format(centimentros,polegadas))