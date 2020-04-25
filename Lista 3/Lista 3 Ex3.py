'3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'

import time
def função():

    letra = input('Digite (M) para masculino e (F) para feminino: ')

    if letra == 'M' or letra == 'm':
        print('Masculino')

    elif letra == 'F' or letra == 'f':
        print('Feminino')

    else:
        print('Sexo inválido. Digite novamente.\n')
        time.sleep(1)
        função()

função()