#3 - Faça um programa que leia e valide as seguintes informações:Nome: maior que 3 caracteres;Idade: entre 0 e 150;Salário: maior que zero;Sexo: 'f' ou 'm';Estado Civil: 's', 'c', 'v', 'd';
x = 0
while x < 1:

    nome = input('\nDigite seu Nome: ')
    tamanho_nome = len(nome)

    if tamanho_nome > 3 or tamanho_nome <= 0:
        x+=1

    else:
        print('\nInforme seu nome novamente...')

while x < 2:

    idade = int(input('Digite sua idade: '))

    if idade > 0 and idade < 150:
        x += 1
    else:
        print('\n Informe sua idade novamente...')

while x < 3:
    salario = float(input('Digite o valor do seu salário: '))

    if salario > 0:
        x+=1
    else:
        print('\n Informe seu salário novamente...')

while x < 4:
    sexo = input('Digite seu sexo (M) ou (F): ')
    nome_list = ['M','m','F','f']

    if sexo in nome_list:
        x+=1
    else:
        print('\n Informe seu sexo novamente...')

while x < 5:
    estado_civil = input('Digite seu estado civil: ')
    estado_civil_list = ['S','s','C','c','V','v','D','d']

    if estado_civil in estado_civil_list:
        x+=1
    else:
        print('\n Informe seu estado civil novamente...')

print('Cadastro concluído!')


