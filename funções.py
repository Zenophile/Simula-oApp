import perfil
from art import ascii_art2, ascii_art3, ascii_art5, ascii_art6, ascii_art7
from perfil import profile, mostra_amigos, lista_amigos
import time
import math

'''
Como este programa não utilizará um GPS de fato, 
utilizaremos o Marco Zero da cidade do Recife como referência. 
Todas as localizações a seguir terão suas distâncias calculadas em relação a este ponto..
------------------------------------------------
Distâncias calculadas através do aplicativo Uber.
'''
locais_recife = {
    "Marco Zero": 0,
    "Shopping Riomar": 3.6,
    "Shopping Boa Vista": 2,
    "Shopping Recife":  7.3,
    "Praça da Jaqueira": 4,
    "Cesar School Brum": 2,
    "Monte Everest": 13540,
}

def apertei_enter_sem_querer(prompt):
    """Estava apertando enter sem querer muitas vezes na hora de testar o código
    então criei esse código que impede isso + umas frescurinhas"""
    while True:
        user_input = input(prompt)
        if user_input.strip():
            try:
                return int(user_input)
            except ValueError:
                print("Por favor, insira um número válido.\n")
        else:
            print("Input não pode estar vazio. Por favor, tente novamente.\n")


def countdown(seconds):
    """#É só uma função que irá contar até x(geralmente 3) antes de voltar quebrar o loop de outra função para retornar ao menu anterior
    assim a mudança de menus fique menus abrupta, não será printado várias letras no console de uma vez."""
    for i in range(seconds, 0, -1):
        print(f'Retornando ao menu anterior em {i}...')
        time.sleep(1)


def adicionar_amigos():
    while True:
        adicionar = input('Digite o nome do seu amigo ou 2 para voltar\n')
        if adicionar == '2':
            break
        else:
            perfil.lista_amigos.append(adicionar)
            print('Amigo adicionado!')
            print(ascii_art7)


amigos_selecionados = set()  # Set to keep track of selected friends

def selecionar_amigo():
    while True:
        print(mostra_amigos())
        try:
            index = int(input('Digite o número do amigo que deseja selecionar (0 para sair): ')) - 1
            if index == -1:  # User input 0 (index will be -1)
                print('Saindo da seleção de amigos.')
                break
            elif 0 <= index < len(lista_amigos):
                amigo_selecionado = lista_amigos[index]
                if amigo_selecionado in amigos_selecionados:
                    print(f'{amigo_selecionado} já foi selecionado. Por favor, selecione outro amigo.')
                else:
                    amigos_selecionados.add(amigo_selecionado)
                    print(f'Amigo selecionado: {amigo_selecionado}')
                    # Optionally do something with the selected friend here
            else:
                print('Índice inválido. Por favor, tente novamente.')
        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')




def display_menu_and_get_selection(locais_recife):
    """Está função é o prato principal da casa!, aqui teremos o menu para mostrar os locais disponíveis, selecionar e seguir
    após isso ela fará alguns cálculos de economia de CO2, distância percorrida etc..."""
    while True:
        km_percorridos = 0
        for i, (key, value) in enumerate(locais_recife.items()):
            print(f"{i}. {key}")
        print("7. Retornar ao menu anterior\n")

        escolha = apertei_enter_sem_querer('...\n')
        if escolha == 7:
            break
        elif escolha is not None and 0 <= escolha < len(locais_recife):
            selected_location = list(locais_recife.items())[escolha]
            n1 = selected_location[1]
            print(f"Você selecionou {selected_location[0]}\n")
            for i, (key, value) in enumerate(locais_recife.items()):
                print(f"{i}. {key}")
            print("7. Cancelar")
            escolha2 = apertei_enter_sem_querer('Escolha o destino.\n')
            if escolha2 == 7:
                print('Cancelando.\n')
                break
            elif escolha2 is not None and 0 <= escolha2 < len(locais_recife) and escolha2 != escolha:
                selected_location = list(locais_recife.items())[escolha2]
                n2 = selected_location[1]
                diff = abs(n1 - n2)
                print(f"Seguindo caminho para {selected_location[0]}\n")
                print(f"A Distância a ser percorrida será de {diff}km\n")
                km_percorridos += diff
                print(ascii_art5)
                perfil.add_km(km_percorridos)
                award = math.floor(km_percorridos / 10)
                perfil.add_award(award)
                co2 = (km_percorridos / 15)
                print(ascii_art6)
                print('Você chegou ao seu destino\n')
                print(f'E deixou de emitir {co2:.2f} gramas de CO2 na nossa atmosfera =) \n')
                while True:
                    menu_escolha = apertei_enter_sem_querer('1. Voltar ao menu anterior \n'
                                                            '2. Sair do aplicativo')
                    if menu_escolha == 1:
                        print('Deseja realizar outra viagem?\n')
                        break
                    elif menu_escolha == 2:
                        print(ascii_art2)
                        exit()
                    else:
                        print('Comando inválido\n')

        else:
            print('Comando inválido')


#Auto explicativo
def escrever_arquivo(nome_arquivo):
    entrada = input('Digite...\n' )
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(entrada + "\n")


#Cadastrar o usuário e senha  separados por vírgula no arquivo .txt
def cadastrar(usuario, senha):
    try:
        with open('usuarios.txt', 'r') as arquivo:
            usuarios = arquivo.readlines()
            for linha in usuarios:
                dados = linha.strip().split(',')
                if len(dados) == 2:
                    existing_username, _ = dados
                    if existing_username == usuario:
                        print('Usuário já existe. Por favor, escolha um nome de usuário diferente.')
                        countdown(3)
                        return


        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(f"{usuario},{senha}\n")
        print("Cadastro realizado com Sucesso!!!")


    except FileNotFoundError:
        # Se o arquivo não existir a função irá cria-lo e adicionar o usuário, muito legal, né!?
        with open('usuarios.txt', 'w') as arquivo:
            arquivo.write(f"{usuario},{senha}\n")
        print("Cadastro realizado com Sucesso!!!")

    print('Digite 1 para retornar à tela de login')
    while True:
        escolha = int(input())
        if escolha == 1:
            break
        else:
            print('Comando inválido')
            continue


#login, sim é case sensitive.
def login(usuario, senha):
    try:
        with open('usuarios.txt', 'r') as arquivo:
            usuarios = arquivo.readlines()
            for linha in usuarios:
                dados = linha.strip().split(',')
                if len(dados) == 2:
                    catch_usuario, catch_senha = dados
                    if catch_usuario == usuario and catch_senha == senha:
                        perfil.usuario_logado = usuario  #essa variável global está no arquivo perfil.py
                        print(f'Bem vindo {usuario}')
                        while True:
                            print('--- MENU ---\n'
                                   '1. Visualizar Perfil\n'
                                   '2. Planejar Rota\n'
                                   '3. Formar Grupo\n'
                                   '4. Adicionar Amigo\n'
                                   '5. Sair.\n')
                            escolha = apertei_enter_sem_querer("")
                            if escolha == 1:
                                profile()
                            elif escolha == 2:
                                rota()
                            elif escolha == 3:
                                selecionar_amigo()
                            elif escolha == 4:
                                adicionar_amigos()

                            elif escolha == 5:
                                print(ascii_art2)
                                exit()
                            else:
                                print('Comando inválido')
                                continue
            print('Usuário ou senha incorretos. Tente novamente.')
            countdown(3)
    except FileNotFoundError:
        print("O arquivo de usuários não foi encontrado.")


#Essa função é basicamente o primeiro menuzinho da Rota que tem a arte ASCII bonitinha, então ela chama a outra função chata lá em cima.

def rota():
    print(ascii_art3)
    while True:
        print('-------- MENU --------\n'
              'Escolha a localização atual digitando o número correspondente.')
        display_menu_and_get_selection(locais_recife)
        break

"""01010110 01001111 01000011 11000011 10001010 00100000 01000101 01010011 01010100 11000011
 10000001 00100000 01010000 01010010 01000101 SOCORRO! 01010011 01001111 00100000 01001110 01000101 
 01010011 01010011 01000101 00100000 01000011 11000011 10010011 01000100 01001001 01000111 
 01001111 00001010"""