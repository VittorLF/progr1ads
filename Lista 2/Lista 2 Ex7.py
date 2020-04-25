'''7. Faça um programa que calcule a área total (m​2​) de uma casa com 4 cômodos. O usuário deve inserir a largura e comprimento de cada um dos cômodos, calcular a área individual de cada um e por fim exibir a área total da casa.
'''

largura_quarto1 = float(input('Digite o valor da largura do quarto 1: '))
comprimento_quarto1 = float(input('Digite o valor do comprimento do quarto 1: '))
largura_quarto2 = float(input('Digite o valor da largura do quarto 2: '))
comprimento_quarto2 = float(input('Digite o valor do comprimento do quarto 2: '))
largura_quarto3 = float(input('Digite o valor da largura do quarto 3: '))
comprimento_quarto3 = float(input('Digite o valor do comprimento do quarto 3: '))
largura_quarto4 = float(input('Digite o valor da largura do quarto 4: '))
comprimento_quarto4 = float(input('Digite o valor do comprimento do quarto 4: '))

m2_quarto1 = float(largura_quarto1 * comprimento_quarto1)
m2_quarto2 = float(largura_quarto2 * comprimento_quarto2)
m2_quarto3 = float(largura_quarto3 * comprimento_quarto3)
m2_quarto4 = float(largura_quarto4 * comprimento_quarto4)
area_total = float(m2_quarto1 + m2_quarto2 + m2_quarto3 + m2_quarto4)

print('A área total da casa é de {}m²'.format(area_total))