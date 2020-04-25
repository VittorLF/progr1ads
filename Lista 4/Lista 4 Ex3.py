#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def dia_da_semana():

    if dia == 1:
        print('1° Dia da semana! [Domingo]')

    elif dia == 2:
        print('2° Dia da semana! [Segunda-Feira]')

    elif dia == 3:
        print('3° Dia da semana! [Terça-Feira]')

    elif dia == 4:
        print('4° Dia da semana! [Quarta-Feira]')

    elif dia == 5:
        print('5° Dia da semana! [Quinta-Feira]')

    elif dia == 6:
        print('6° Dia da semana! [Sexta-Feira]')
        print('SEXTOUUU PAPAII...Ops!!....Quarentena')

    elif dia == 7:
        print('7° Dia da semana! [Sábado]')

    else:
        print('Numero Inválido!! Tente Novamente\n')

        dia_da_semana()

dia = int(input('Digite um número de (1 a 7) para saber o dia da semana correspondente: '))

dia_da_semana()
