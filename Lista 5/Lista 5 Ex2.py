# 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir asinformações

while True:

    usuario = input('\nUsuário: ')
    senha = input('\nSenha: ')

    if senha == usuario:
        print('\nDigite uma senha diferente do nome de usuário!')
        continue
    else:
        print('Login concluído.')
        break
