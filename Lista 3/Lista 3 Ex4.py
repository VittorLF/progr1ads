'4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'

def função():

    letra = input('Digite a letra para saber se é uma Vogal ou Consoante: ')

    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('É uma vogal.')

    elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print('É uma vogal')

    else:
        print('É uma consoante.')

função()