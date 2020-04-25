'''9. Escreva um programa que converte valores de polegadas em centímetros utilizando a seguinte fórmula para conversão: 1 polegada = 2,54 cm;'''

polegadas = float(input('Digite o valor em polegadas: '))

centimetros = polegadas * 2.54

print('{} polegadas é {:.2f} centimetros'.format(polegadas,centimetros))
