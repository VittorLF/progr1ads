'''3. Faça um programa que calcule a média de consumo de combustível de um veículo. O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.
'''

km_inicial = float(input('Informe o KM inicial: '))
km_final = float(input('Informe o KM final: '))
litros = float(input('Informe quantos litros foram gastos: '))

total = (km_final - km_inicial)/litros

print('A quantidade média de combustível gasto foi {:.2f}L/Km'.format(total))