'''10. Faça um programa que calcula o novo valor do salário de um funcionário. O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).'''

salario_atual = float(input('Digite o salário atual: '))
reajuste = float(input('Digite o percentual de reajuste: '))

total = salario_atual + (salario_atual * reajuste/100)

print('O valor do seu salário agora é de R${:.2f}'.format(total))
