#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# - Salário Bruto até 900 (inclusive) - isento
# - Salário Bruto até 1500 (inclusive) - desconto de 5%
# - Salário Bruto até 2500 (inclusive) - desconto de 10%
# - Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valor_hora = float(input('Informe o valor da Hora: '))
quantidade_horas = float(input('Informe a quantidade de horas trabalhadas: '))

salario_bruto = (valor_hora * quantidade_horas)
inss = (salario_bruto * 10/100)
fgts = (salario_bruto * 11/100)


#imposto de renda
if salario_bruto < 900:
    ir = 0
    porcent = 0

elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = (salario_bruto * 5/100)
    porcent = 5

elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = (salario_bruto * 10/100)
    porcent = 10

elif salario_bruto > 2500:
    ir = (salario_bruto * 20/100)
    porcent = 20

total_descontos = inss + ir
salario_liquido = salario_bruto - total_descontos
print('-=-'*20)
print('Salário Bruto  --------- R${:.2f}'.format(salario_bruto))
print('(-) IR ({}%)   --------- R${:.2f}'.format(porcent,ir))
print('(-) INSS (10%) --------- R${:.2f}'.format(inss))
print('FGTS (11%)     --------- R${:.2f}'.format(fgts))
print('Total de Descontos ----- R${:.2f}'.format(total_descontos))
print('Salário Líquido -------- R${:.2f}'.format(salario_liquido))
print('-=-'*20)
