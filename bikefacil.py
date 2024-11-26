import perfil
from funções import cadastrar, login, apertei_enter_sem_querer
from art import ascii_art2, ascii_art4

#o arquivo bikefacil vulgo main.py é basicamente o primeiro menu do app, a bagunça(funções) estão no arquivo funções.py
def print_usuario_logado():
    if perfil.usuario_logado:
        print(f'Usuário logado: {perfil.usuario_logado}')
    else:
        print("Nenhum usuário está logado atualmente")
print(ascii_art4)
'''Esse é o primeiro while loop do código, a partir daqui teremos vários whiles que serão iniciados pelas funções.
Então sempre que o código voltar para o menu anterior ele simplesmente estará quebrando o while loop atual, exit().
'''

while True:
    print("--- MENU --- \n"
          "1. para Login\n"
          "2. para Cadastrar usuário\n"
          "3. para Sair\n"
          "Escolha uma opção\n")
    escolha = apertei_enter_sem_querer("")

    if escolha == 1:
        user = input('Digite o usuário\n')
        senha = input('Digite a senha\n')
        login(user, senha)
        print_usuario_logado()
    elif escolha == 2:
        user = input('Digite o usuario\n')
        senha = input('Digite a senha\n')
        cadastrar(user, senha)
        continue

    elif escolha == 3:
        print(ascii_art2)
        break

    else:
        print('Opção inválida')
        continue