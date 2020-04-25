#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Entre 9.0 e 10.0        A
#Entre 7.5 e 9.0         B
#Entre 6.0 e 7.5         C
#Entre 4.0 e 6.0         D
# Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o conceito for D ou E.

def media_aluno():

    resultado = (nota1 + nota2) / 2

    if resultado >= 9 and resultado <= 10:
        print('-=-'* 10)#visual
        print('Parabens, classifacação [A] atingida.')
        print('-=-' * 10)#visual
        print('Nota média final de {}'.format(resultado))
        print('-=-' * 10)#visual
        print('!!Aprovado!!')
        print('-=-' * 10)#visual

    elif resultado >= 7.5 and resultado < 9:
        print('-=-' * 10)#visual
        print('Parabens, classifacação [B] atingida.')
        print('-=-' * 10)#visual
        print('Nota média final de {}'.format(resultado))
        print('-=-' * 10)#visual
        print('!!Aprovado!!')
        print('-=-' * 10)#visual

    elif resultado >= 6 and resultado < 7.5:
        print('-=-' * 10)  # visual
        print('Parabens, classifacação [C] atingida.')
        print('-=-' * 10)  # visual
        print('Nota média final de {}'.format(resultado))
        print('-=-' * 10)  # visual
        print('!!Aprovado!!')
        print('-=-' * 10)  # visual

    elif resultado >= 4 and resultado < 6:
        print('-=-' * 10)  # visual
        print('Classifacação [D] atingida.')
        print('-=-' * 10)  # visual
        print('Nota média final de {}'.format(resultado))
        print('-=-' * 10)  # visual
        print('Reprovado')
        print('-=-' * 10)  # visual

    elif resultado >= 0 and resultado < 4:
        print('-=-' * 10)  # visual
        print('Classifacação [E] atingida.')
        print('-=-' * 10)  # visual
        print('Nota média final de {}'.format(resultado))
        print('-=-' * 10)  # visual
        print('Reprovado')
        print('-=-' * 10)  # visual

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media_aluno()
