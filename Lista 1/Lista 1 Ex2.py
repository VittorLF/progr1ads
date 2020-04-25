''' 2 - Sabendo que a cotação atual do dólar americano é R$ 4,47, receba um valor em reais do
 usuário e converta para dólares. Exemplo de saída: $ 1.00
'''

valor = float(input('Digite o valor em reais R$: '))

dolar = valor * 4.47

print('${:.2f}'.format(dolar))
