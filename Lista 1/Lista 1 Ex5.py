'''5 - Receba do usuário o ano em que estamos, e o ano que ele nasceu, e calcule sua idade.
Despreze os meses.'''

ano = int(input('Digite o ano atual: '))
nascimento = int(input('Digite o ano que nasceu: '))

idade = ano - nascimento

print('Você tem {} anos'.format(idade))
