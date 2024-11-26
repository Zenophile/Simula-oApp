from art import ascii_art

usuario_logado = None
total_km = 0
total_award = 0

'''add_km e add_award são funções que irão lidar com variáveis globais que armazenarão o desempenho do usuário
como kms percorridos e troféus, a cada 10km percorridos o usuário recebe um award em seu perfil, 
inflará o seu ego tanto quanto um like naquele seu story do insta, mas em adicional você também irá emagrecer =)'''

def add_km(km):
    global total_km
    total_km += km

def add_award(award):
    global total_award
    total_award += award / 10

def profile():
    while True:
        amigos = 0 #Cara, isso é muito triste!
        print(f'{ascii_art}')
        print(f'Olá {usuario_logado}\n'
              f'KM PERCORRIDOS: {total_km}\n'
              f'TROFÉUS: {total_award}\n'
              f'Amigos: {amigos}\n')
        escolha = int(input('1. Retornar ao Menu anterior'))
        if escolha == 1:
            break
        else:
            print('Opção inválida')









































