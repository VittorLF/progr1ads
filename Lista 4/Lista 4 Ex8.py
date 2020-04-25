# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Informe o Dia: '))
mes = int(input('Informe o Mês: '))
ano = int(input('Informe o Ano: '))

data_valida = False



if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):

    if (dia <= 31):

        data_valida = True

elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):

    if (dia <= 30):

        data_valida = True

elif mes == 2:

    if (ano % 4 == 0 and ano % 400 != 0) or (ano % 400 == 0):
        if (dia <= 29):

            data_valida = True

    elif (dia <= 28):

        data_valida = True

if (data_valida):

    print('A data é válida')
else:

    print('A data é Inválida')
