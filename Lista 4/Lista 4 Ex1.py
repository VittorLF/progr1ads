#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#- Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#-- salários até R$ 280,00 (incluindo) : aumento de 20%
#-- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#-- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#-- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#-- o salário antes do reajuste;
#-- o percentual de aumento aplicado;
#-- o valor do aumento;
#-- o novo salário, após o aumento.

salario_atual = float(input('Informe o valor do salário atual: '))

if salario_atual <= 280:
    novo_salario = salario_atual + (salario_atual * (20/100))
    difereça = novo_salario - salario_atual
    print('O valor de R${:.2f}, teve um reajuste de 20% e subiu para R${:.2f}, acrescimo de R${:.2f}.'.format(salario_atual, novo_salario, difereça))

elif salario_atual > 280 and salario_atual < 700:
    novo_salario = salario_atual + (salario_atual * (15/100))
    difereça = novo_salario - salario_atual
    print('O valor de R${:.2f}, teve um reajuste de 15% e subiu para R${:.2f}, acrescimo de R${:.2f}.'.format(salario_atual, novo_salario, difereça))

elif salario_atual >= 700 and salario_atual < 1500:
    novo_salario = salario_atual + (salario_atual * (10 / 100))
    difereça = novo_salario - salario_atual
    print('O valor de R${:.2f}, teve um reajuste de 10% e subiu para R${:.2f}, acrescimo de R${:.2f}.'.format(salario_atual, novo_salario, difereça))

elif salario_atual >= 1500:
    novo_salario = salario_atual + (salario_atual * (5 / 100))
    difereça = novo_salario - salario_atual
    print('O valor de R${:.2f}, teve um reajuste de 5% e subiu para R${:.2f}, acrescimo de R${:.2f}.'.format(salario_atual, novo_salario, difereça))
