# 10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def função():

        print('Digite o turno que você estuda...')
        turno = input('(M) para matutino, (V) para vespertino e (N) para Noturno: ')

        if turno == 'M' or turno == 'm':
            print('\nBom Dia!!')

        elif turno == 'V' or turno == 'v':
            print('\nBoa Tarde!!')

        elif turno == 'N' or turno == 'n':
            print('\nBoa Noite!!')

função()