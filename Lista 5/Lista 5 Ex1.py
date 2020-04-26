# 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem casoo valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    user = float(input('Insira um numero entre zero e dez: '))
    if user >= 0 and user <= 10:
        print(user)

        break
    else:
        print('Informe um valor válido')