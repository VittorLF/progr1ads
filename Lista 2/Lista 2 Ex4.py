'''4. Escreva um programa que leia uma temperatura em graus Fahrenheit, transforme-a em graus Celsius e exiba o resultado.'''

fahren = float(input('Digite os graus em Fahrenheit: '))

celsius = (fahren - 32) * 5/9

print('Em celsius são: {:.2f}°C'.format(celsius))
